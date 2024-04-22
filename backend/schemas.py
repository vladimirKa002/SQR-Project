from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    email: str

class Item(BaseModel):
    id: int
    name: str
    description: str
    price: int

class Template(BaseModel):
    id: int
    name: str
    description: str

class TierList(BaseModel):
    id: int
    user_id: int
    template_id: int

class TemplateItem(BaseModel):
    template_id: int
    item_id: int

class TierListItem(BaseModel):
    tier_list_id: int
    item_id: int

class Tier(BaseModel):
    tier: str


