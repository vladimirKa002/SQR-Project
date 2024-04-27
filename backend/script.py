from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models import User, Item, Template, TierList, TierListItem, Tier, template_item
from sqlalchemy import create_engine, MetaData
from sqlalchemy.engine.reflection import Inspector
# Import settings from config.py
from config import DEFAULT_SETTINGS
import random
from PIL import Image
import io


def generate_random_items(n):
    """Generate n random items with a simple image."""
    colors = {
        'Red': (255, 0, 0),
        'Blue': (0, 0, 255),
        'Green': (0, 255, 0),
        'Yellow': (255, 255, 0),
        'Black': (0, 0, 0),
        'White': (255, 255, 255)
    }
    sizes = ['small', 'medium', 'large', 'extra large']
    base_price = 100  # Base price for items

    for _ in range(n):
        color_name, rgb = random.choice(list(colors.items()))
        size = random.choice(sizes)
        name = f"{color_name} Pizza"
        description = f"A {size} {color_name.lower()} pizza"
        price = base_price + random.randint(-20, 50)  # Randomize price a bit

        # Create an image with PIL
        img = Image.new('RGB', (100, 100), color=rgb)
        byte_arr = io.BytesIO()
        img.save(byte_arr, format='PNG')
        
        yield Item(name=name, description=description, price=price, picture=byte_arr.getvalue())


def print_structure():
    meta = MetaData()
    meta.reflect(bind=engine)
    for table in meta.tables.values():
        print(f"Table Name: {table.name}")
        for column in table.c:
            print(f"  Column Name: {column.name} - Type: {column.type}")


# Create an engine that stores data in the local directory's app.db file.
engine = create_engine(DEFAULT_SETTINGS.database_uri)


# Base class for your models
Base = declarative_base()

# Create session
Session = sessionmaker(bind=engine)
session = Session()


# Items
item_list = []
item_generator = generate_random_items(5)
for item in item_generator:
    print(f"Item: {item.name}, Description: {item.description}, Price: {item.price}, Picture data length: {len(item.picture)}")
    item_list.append(item)
# Templates
print(item_list)
template1 = Template(name='Basic Template', picture=b'basictemplatepic')


# Insert users, items, and tiers into the database
session.add_all(item_list)
session.add_all([template1])
session.commit()
print("checkpoint")

# Template items mapping (association table)
session.execute(template_item.insert().values(template_id=template1.id, item_id=item_list[1]))
session.execute(template_item.insert().values(template_id=template1.id, item_id=item_list[2]))
session.commit()

# Close session
session.close()

print("Sample data created successfully!")
