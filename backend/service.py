from fastapi import Depends

import models
import schemas
from backend.database import get_db
from backend.security import manager
from main import app


@app.get("/template/all", response_model=list[schemas.Template])
def get_all_templates(db=Depends(get_db)):
    return db.query(models.Template).all()


@app.get("/template/{template_id}", response_model=schemas.Template)
def get_template(template_id: int, db=Depends(get_db)):
    return db.query(models.Template).where(models.Template.id == template_id).first()


@app.post("/template/create", response_model=schemas.Template)
def create_template(template: schemas.TemplateCreate, db=Depends(get_db)):
    template = schemas.TemplateCreate(name=template.name)
    db.add(template)
    db.commit()
    return template


@app.get("/item/{item_id}", response_model=schemas.Item)
def get_food(item_id: int, db=Depends(get_db)):
    return db.query(models.Item).where(models.Item.id == item_id).first()


# Create item


@app.get("/tierlist/all", response_model=list[schemas.TierList])
def get_all_tierlists(user=Depends(manager), db=Depends(get_db)):
    return db.query(models.TierList).where(models.TierList.user_id == user.id).all()


@app.get("/tierlist/{template_id}", response_model=schemas.Template)
def get_tierlist(template_id: int, user=Depends(manager), db=Depends(get_db)):
    return db.query(models.TierList).where(models.TierList.user_id == user.id
                                           and models.TierList.template_id == template_id).first()


# Create tier list
