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

def get_file_names(directory):
    """Return a list of file names in the given directory."""
    # List all entries in the directory
    entries = os.listdir(directory)
    # Filter entries to include files only, excluding directories
    file_names = [entry for entry in entries if os.path.isfile(os.path.join(directory, entry))]
    return file_names

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def generate_random_items(n):
    """Generate n random items with a simple image."""

    for _ in range(n):
        size = random.choice(sizes)
        name = f"{color_name} Pizza"
        description = f"A {size} {color_name.lower()} pizza"
        price = base_price + random.randint(-20, 50)  # Randomize price a bit
    
        yield Item(name=name, description=description, price=price, picture=convertToBinaryData('images/apple.png'))


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
print (item_list[0])
# Template items mapping (association table)
session.execute(template_item.insert().values(template_id=template1.id, item_id=item_list[0].id))
# session.execute(template_item.insert().values(template_id=template1.id, item_id=item_list[2]))
session.commit()

# Close session
session.close()

print("Sample data created successfully!")
