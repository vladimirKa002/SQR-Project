from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException
from sqlalchemy import inspect

from config import DEFAULT_SETTINGS
from schemas import UserCreate, UserResponse
from database import get_db, Base, engine
from database_actions import get_user, create_user
from security import manager, verify_password

from service import router as service_router


app = FastAPI()
app.include_router(service_router)


@app.on_event("startup")
def setup():
    print("Creating db tables...")
    Base.metadata.create_all(bind=engine)
    inspection = inspect(engine)
    print(f"Created {len(inspection.get_table_names())} tables: {inspection.get_table_names()}")


@app.post("/auth/register")
def register(user: UserCreate, db=Depends(get_db)):
    if get_user(user.email) is not None:
        raise HTTPException(status_code=400, detail="A user with this email already exists")
    else:
        db_user = create_user(db, user)
        return UserResponse(id=db_user.id, email=db_user.email, name=db_user.name)


@app.post(DEFAULT_SETTINGS.token_url)
def login(data: OAuth2PasswordRequestForm = Depends()):
    email = data.username
    password = data.password

    user = get_user(email)  # we are using the same function to retrieve the user
    if user is None:
        raise InvalidCredentialsException  # you can also use your own HTTPException
    elif not verify_password(password, user.password):
        raise InvalidCredentialsException

    access_token = manager.create_access_token(
        data=dict(sub=user.email)
    )
    return {'access_token': access_token, 'token_type': 'Bearer'}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app")
