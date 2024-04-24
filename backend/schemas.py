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
