from pydantic import ConfigDict, BaseModel, EmailStr


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    model_config = ConfigDict(from_attributes=True)


class Item(BaseModel):
    id: int
    name: str
    description: str
    price: int
    # picture


class Tier(BaseModel):
    tier: str


class TierListItem(BaseModel):
    tier_list_id: int
    item_id: int
    tier: Tier


class Template(BaseModel):
    id: int
    name: str
    items: list[Item] = []
    # picture (cover)


class TemplateCreate(BaseModel):
    id: int
    name: str
    # picture (cover)


class TierList(BaseModel):
    id: int
    template: Template
    items: list[TierListItem] = []
