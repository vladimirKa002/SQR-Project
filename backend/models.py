from database import Base
from sqlalchemy import String, Column, Integer, ForeignKey
from fastapi_utils.guid_type import GUID, GUID_DEFAULT_SQLITE
from sqlalchemy.orm import relationship

import passlib.hash as _hash


class User(Base):
    __tablename__ = "users"
    id = Column(GUID, primary_key=True, default=GUID_DEFAULT_SQLITE)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    def verify_password(self, password: str):
        return _hash.bcrypt.verify(password, self.hashed_password)


class Item(Base):
    __tablename__ = "items"
    id = Column(GUID, primary_key=True, default=GUID_DEFAULT_SQLITE)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Integer, nullable=False)


class Template(Base):
    __tablename__ = "templates"
    id = Column(GUID, primary_key=True, default=GUID_DEFAULT_SQLITE)
    name = Column(String, nullable=False)
    description = Column(String)


class TierList(Base):
    __tablename__ = "tier_lists"
    id = Column(GUID, primary_key=True, default=GUID_DEFAULT_SQLITE)
    user_id = Column(GUID, ForeignKey('users.id'), nullable=False)
    template_id = Column(GUID, ForeignKey('templates.id'), nullable=False)

    # Define relationships
    user = relationship("User")
    template = relationship("Template")


class TemplateItem(Base):
    __tablename__ = "template_items"
    template_id = Column(GUID, ForeignKey('templates.id'), nullable=False, primary_key=True)
    item_id = Column(GUID, ForeignKey('items.id'), nullable=False, primary_key=True)

    # Define relationships
    template = relationship("Template")
    item = relationship("Item")


class TierListItem(Base):
    __tablename__ = "tier_list_items"
    tier_list_id = Column(GUID, ForeignKey('tier_lists.id'), nullable=False, primary_key=True)
    item_id = Column(GUID, ForeignKey('items.id'), nullable=False, primary_key=True)

    # Define relationships
    tier_list = relationship("TierList")
    item = relationship("Item")


class Tier(Base):
    __tablename__ = "tiers"
    tier = Column(GUID, primary_key=True, default=GUID_DEFAULT_SQLITE)
