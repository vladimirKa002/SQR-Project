# https://tutorial101.blogspot.com/2023/03/fastapi-jwt-token-authentication-with.html
import fastapi as _fastapi
import fastapi.security as _security
import jwt as _jwt
import sqlalchemy.orm as _orm
import passlib.hash as _hash

import database as _database, models as _models, schemas as _schemas

oauth2schema = _security.OAuth2PasswordBearer(tokenUrl="/users/token")

JWT_SECRET = "innofoodtierlist"


def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)


def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_user_by_email(email: str, db: _orm.Session):
    return db.query(_models.User).filter(_models.User.email == email).first()


async def create_user(user: _schemas.UserCreate, db: _orm.Session):
    user_obj = _models.User(
        name=user.name,
        email=user.email,
        hashed_password=_hash.bcrypt.hash(user.password)
    )
    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
    return user_obj


async def authenticate_user(email: str, password: str, db: _orm.Session):
    user = await get_user_by_email(db=db, email=email)

    if not user:
        return False
    if not user.verify_password(password):
        return False
    return user


async def create_token(user: _models.User):
    user_obj = _schemas.User.from_orm(user)

    token = _jwt.encode(user_obj.dict(), JWT_SECRET)

    return dict(access_token=token, token_type="bearer")


async def get_current_user(
        db: _orm.Session = _fastapi.Depends(get_db),
        token: str = _fastapi.Depends(oauth2schema),
):
    try:
        payload = _jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        user = db.query(_models.User).get(payload["id"])
    except:
        raise _fastapi.HTTPException(
            status_code=401, detail="Invalid Email or Password"
        )

    return _schemas.User.from_orm(user)


async def get_item(item_id: int, db:  _orm.Session):
    return db.query(_models.Item).filter(_models.Item.email == item_id).first()


def get_template(template_id: int, db: _orm.Session):
    # Query the template by ID including its related items
    template = db.query(_models.Template).filter(_models.Template.id == template_id).first()
    if not template:
        raise _fastapi.HTTPException(status_code=404, detail="Template is not found")
    return template


# def get_tierlist(tierlist_id: int, db: _orm.Session):
#     # Query the template by ID including its related items
#     tierlist = db.query(_models.Tierlist).filter(_models.Tierlist.id == tierlist_id).first()
#     if not tierlist:
#         raise _fastapi.HTTPException(status_code=404, detail="Tierlist is not found")
#     return tierlist