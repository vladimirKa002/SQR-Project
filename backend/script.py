from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models import User, Item, Template, TierList, TierListItem, Tier, template_item
from sqlalchemy import create_engine, MetaData
from sqlalchemy.engine.reflection import Inspector
# Import settings from config.py
from config import DEFAULT_SETTINGS

# Create an engine that stores data in the local directory's app.db file.
engine = create_engine(DEFAULT_SETTINGS.database_uri)
# meta = MetaData()

# meta.reflect(bind=engine)
# for table in meta.tables.values():
#     print(f"Table Name: {table.name}")
#     for column in table.c:
#         print(f"  Column Name: {column.name} - Type: {column.type}")
# Base class for your models
Base = declarative_base()

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Create sample data
# Users
user1 = User(name='Alice', email='alice@example.com', password='alicepass')
user2 = User(name='Bob', email='bob@example.com', password='bobpass')

# Items
item1 = Item(name='Red Widget', description='A small red widget', price=100, picture=b'redwidgetpic')
item2 = Item(name='Blue Widget', description='A large blue widget', price=150, picture=b'redwidgetpic')

# Templates
template1 = Template(name='Basic Template', picture=b'basictemplatepic')

# Tier
# tier1 = Tier(tier='S')
# tier2 = Tier(tier='A')

# Insert users, items, and tiers into the database
session.add_all([user1, user2, item1, item2, template1])
session.commit()

# Template items mapping (association table)
session.execute(template_item.insert().values(template_id=template1.id, item_id=item1.id))
session.execute(template_item.insert().values(template_id=template1.id, item_id=item2.id))

# # Tier Lists
# tier_list1 = TierList(user_id=user1.id, template_id=template1.id)

# # Tier List Items
# tier_list_item1 = TierListItem(tier_list_id=tier_list1.id, item_id=item1.id, tier_value=tier1.tier)
# tier_list_item2 = TierListItem(tier_list_id=tier_list1.id, item_id=item2.id, tier_value=tier2.tier)

# # Insert tier lists and tier list items
# session.add_all([tier_list1, tier_list_item1, tier_list_item2])
session.commit()

# Close session
session.close()

print("Sample data created successfully!")
