import base64
import os
import random

from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Import settings from config.py
from models import Item, Template, template_item
from config import DEFAULT_SETTINGS


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
        blobData = base64.b64encode(blobData)
    return blobData


def print_structure():
    meta = MetaData()
    meta.reflect(bind=engine)
    for table in meta.tables.values():
        print(f"Table Name: {table.name}")
        for column in table.c:
            print(f"  Column Name: {column.name} - Type: {column.type}")


def generate_random_to_product_index(n):
    return random.choice(range(n + 1))


# Create an engine that stores data in the local directory's app.db file.
engine = create_engine(DEFAULT_SETTINGS.database_uri)


# Base class for your models
Base = declarative_base()

# Create session
Session = sessionmaker(bind=engine)
session = Session()


products = [
    ('apple.png', 'A fresh red apple, crisp and sweet.', 150),
    ('bread.png', 'A loaf of freshly baked bread, soft and warm.', 120),
    ('cabbage.png', 'A head of green cabbage, rich in nutrients.', 100),
    ('cake.png', 'A slice of chocolate cake, rich and moist.', 250),
    ('cantaloupe.png', 'A ripe cantaloupe, sweet and juicy.', 200),
    ('carrots.png', 'A bunch of vibrant, fresh carrots.', 110),
    ('chicken.png', 'A whole roasted chicken, tender and flavorful.', 350),
    ('choco-chip.png', 'Chocolate chip cookies, homemade and delicious.', 180),
    ('coffee-glass.png', 'A glass of iced coffee, chilled and refreshing.', 220),
    ('cucumber-slice.png', 'Sliced cucumber, cool and crunchy.', 100),
    ('eggplant.png', 'A fresh eggplant, smooth and shiny.', 150),
    ('figs.png', 'Fresh figs, sweet and succulent.', 250),
    ('french-fries.png', 'Crispy French fries, golden and salted.', 130),
    ('fried-chicken.png', 'Crispy fried chicken, juicy and spicy.', 300),
    ('grapefruit.png', 'A fresh grapefruit, tart and juicy.', 160),
    ('hot-dog.png', 'A classic hot dog, fully loaded with toppings.', 190),
    ('kebab.png', 'A skewer of kebab, grilled to perfection.', 320),
    ('kiwi.png', 'A ripe kiwi, tangy and sweet.', 140),
    ('macaron.png', 'Colorful macarons, light and airy.', 210),
    ('mushrooms.png', 'Fresh mushrooms, earthy and aromatic.', 130),
    ('pancake.png', 'Stack of pancakes, fluffy and served with syrup.', 180),
    ('paprika.png', 'Bright red paprika, spicy and flavorful.', 150),
    ('pineapple.png', 'A fresh pineapple, tropical and sweet.', 200),
    ('pizza.png', 'A slice of pepperoni pizza, cheesy and savory.', 250),
    ('pomegranate.png', 'Fresh pomegranate, tart and juicy seeds.', 280),
    ('spaghetti.png', 'Plate of spaghetti, topped with marinara sauce.', 320),
    ('strawberry-milk.png', 'Strawberry milk, creamy and sweet.', 170),
    ('strawberry.png', 'Fresh strawberries, bright and sweet.', 160),
    ('taco.png', 'A beef taco, spicy and filled with fresh vegetables.', 220),
    ('tomato-slice.png', 'Sliced tomatoes, ripe and juicy.', 110),
    ('watermelon.png', 'A slice of watermelon, refreshing and sweet.', 130)
]
image_directory = 'images/'
item_list = []
# Process each image file, description, and price triplet, creating an Item for each
for file_name, description, price in products:
    full_path = os.path.join(image_directory, file_name)
    picture_blob = convertToBinaryData(full_path)
    item_name = file_name[:-4].replace('-', ' ').replace('_', ' ').title()
    item = Item(name=item_name, description=description, price=price, picture=picture_blob)
    item_list.append(item)
    session.add(item)

template_info = [
    ('Cup and Cake Cafe', 'cupncake.png'),
    ('Fresh Brew Coffee', 'fresh.png'),
    ('Super Fresh', 'fresh.png')
]
template_info_list = []
image_cafes_directory = 'images/cafes/'

for template_info_item in template_info:
    full_path = os.path.join(image_cafes_directory, template_info_item[1])
    picture_blob = convertToBinaryData(full_path)
    template = Template(name=template_info_item[0], picture=picture_blob)
    session.add(template)
    template_info_list.append(template)

session.commit()
# Template items mapping (association table)

for i in range(0, 3):
    # insert random items to template
    for j in range(0, 10):
        print(i, j)
        print(template_info_list[i].id, item_list[generate_random_to_product_index(len(products)-1)].id)
        session.execute(template_item.insert().values(template_id=template_info_list[i].id, item_id=item_list[generate_random_to_product_index(len(products)-1)].id))
# session.execute(template_item.insert().values(template_id=template1.id, item_id=item_list[2]))
session.commit()

# Close session
session.close()

print("Sample data created successfully!")
