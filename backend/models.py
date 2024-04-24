from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)


class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Integer, nullable=False)


class Template(Base):
    __tablename__ = "templates"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)


class TierList(Base):
    __tablename__ = "tier_lists"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    template_id = Column(Integer, ForeignKey('templates.id'), nullable=False)

    # Define relationships
    user = relationship("User")
    template = relationship("Template")


class TemplateItem(Base):
    __tablename__ = "template_items"
    template_id = Column(Integer, ForeignKey('templates.id'), nullable=False, primary_key=True)
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False, primary_key=True)

    # Define relationships
    template = relationship("Template")
    item = relationship("Item")


class TierListItem(Base):
    __tablename__ = "tier_list_items"
    tier_list_id = Column(Integer, ForeignKey('tier_lists.id'), nullable=False, primary_key=True)
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False, primary_key=True)

    # Define relationships
    tier_list = relationship("TierList")
    item = relationship("Item")


class Tier(Base):
    __tablename__ = "tiers"
    tier = Column(Integer, primary_key=True)
