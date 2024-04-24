from pydantic import BaseModel


class _UserBase(BaseModel):
    name: str
    email: str


class UserCreate(_UserBase):
    password: str

    class Config:
        orm_mode = True


class User(_UserBase):
    id: int

    class Config:
        orm_mode = True


class Item(BaseModel):
    id: int
    name: str
    description: str
    price: int


class TierListItem(BaseModel):
    tier_list_id: int
    item_id: int


class TierList(BaseModel):
    id: int
    user_id: int
    template_id: int
    items: list[Item] = []


class TemplateItem(BaseModel):
    template_id: int
    item_id: int


class Template(BaseModel):
    id: int
    name: str
    description: str
    items: list[TemplateItem] = []


class Tier(BaseModel):
    tier: str
