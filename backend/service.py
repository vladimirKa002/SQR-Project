from fastapi import Depends, APIRouter

import requests
import models
import schemas
from database import get_db
from security import manager


router = APIRouter()


@router.get("/template/all", response_model=list[schemas.Template])
def get_all_templates(db=Depends(get_db)):
    return db.query(models.Template).all()


@router.get("/template/{template_id}", response_model=schemas.Template)
def get_template(template_id: int, db=Depends(get_db)):
    return db.query(models.Template).where(models.Template.id == template_id).first()


@router.post("/template/create", response_model=schemas.Template)
def create_template(template: schemas.TemplateCreate, db=Depends(get_db)):
    template = schemas.TemplateCreate(name=template.name, picture=template.picture)
    db.add(template)
    db.commit()
    return template


@router.get("/item/{item_id}", response_model=schemas.Item)
def get_food(item_id: int, db=Depends(get_db)):
    return db.query(models.Item).where(models.Item.id == item_id).first()


# Create item
@router.post("/item/create", response_model=schemas.Item)
def create_item(item: schemas.Item, db=Depends(get_db)):
    item = schemas.Item(
        name=item.name, description=item.description, price=item.price, picture=item.picture
    )
    db.add(item)
    db.commit()
    return item


@router.get("/tierlist/all", response_model=list[schemas.TierList])
def get_all_tierlists(user=Depends(manager), db=Depends(get_db)):
    return db.query(models.TierList).where(models.TierList.user_id == user.id).all()


@router.get("/tierlist/{template_id}", response_model=schemas.Template)
def get_tierlist(template_id: int, user=Depends(manager), db=Depends(get_db)):
    return db.query(models.TierList).where(models.TierList.user_id == user.id
                                           and models.TierList.template_id == template_id).first()


# Create tier list
@router.post("/tier_list/create", response_model=schemas.TierList)
def create_item(tier_list: schemas.TierListCreate, db=Depends(get_db)):
    existing_tier_list = db.query(models.TierList).filter(
        models.TierList.user_id == tier_list.user_id
    ).first()

    if existing_tier_list:
        # If the tier list already exists, return it
        return existing_tier_list

    tier_list = schemas.TierListCreate(template=tier_list.template)
    db.add(tier_list)
    db.commit()
    return tier_list


@router.get("/fact")
def get_fact(language="en"):
    url = f"https://uselessfacts.jsph.pl/api/v2/facts/today?language={language}"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data["text"]
    else:
        return "Failed to fetch today's useless fact"
