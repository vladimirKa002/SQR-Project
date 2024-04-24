import fastapi as _fastapi
import fastapi.security as _security

import sqlalchemy.orm as _orm

import services as _services, schemas as _schemas

app = _fastapi.FastAPI()


@app.post("/users/register")
async def register(
        user: _schemas.UserCreate, db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    db_user = await _services.get_user_by_email(user.email, db)
    if db_user:
        raise _fastapi.HTTPException(status_code=400, detail="Email already in use")

    user = await _services.create_user(user, db)

    return await _services.create_token(user)


@app.post("/users/login")
async def login(
        form_data: _security.OAuth2PasswordRequestForm = _fastapi.Depends(),
        db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    user = await _services.authenticate_user(form_data.username, form_data.password, db)

    if not user:
        raise _fastapi.HTTPException(status_code=401, detail="Invalid Credentials")

    return await _services.create_token(user)


@app.get("/users/profile", response_model=_schemas.User)
async def get_user(user: _schemas.User = _fastapi.Depends(_services.get_current_user)):
    return user


# @app.get("/templates", response_model=list[_schemas.Template])
# async def get_all_templates(db: _orm.Session):
#     """
#     Fetches all templates, returning only their IDs and names.
#     """
#     templates = db.query(_schemas.Template.id, _schemas.Template.name).all()
#     return [_schemas.Template(id=template.id, name=template.name) for template in templates]


# @app.get("/tierlists", response_model=list[_schemas.Tierlist])
# async def get_all_tierlists(db: _orm.Session):
#     """
#     Returns all tierlists.
#     """
#     tierlists = db.query(_schemas.Tierlist.id, _schemas.Tierlist.name).all()
#     return [_schemas.Template(id=tierlist.id, name=tierlist.name) for tierlist in tierlists]


@app.get("/templates/{template_id}", response_model=_schemas.Template)
async def get_template(template: _schemas.Template = _fastapi.Depends(_services.get_template)):
    return template


# @app.get("/tierlists/{template_id}", response_model=_schemas.Template)
# async def get_tierlist(template: _schemas.Template = _fastapi.Depends(_services.get_tierlist)):
#     return template