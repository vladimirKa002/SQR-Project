import sqlite3

conn = sqlite3.connect('foodtierlist.db')
c = conn.cursor()

c.execute('''CREATE TABLE "tiers" (
    tier TEXT PRIMARY KEY
)''')

c.execute("INSERT INTO tiers (tier) VALUES ('S')")
c.execute("INSERT INTO tiers (tier) VALUES ('A')")
c.execute("INSERT INTO tiers (tier) VALUES ('B')")
c.execute("INSERT INTO tiers (tier) VALUES ('C')")
c.execute("INSERT INTO tiers (tier) VALUES ('D')")
c.execute("INSERT INTO tiers (tier) VALUES ('E')")
c.execute("INSERT INTO tiers (tier) VALUES ('F')")

c.execute(
    '''CREATE TABLE "users" (
        "id"	INTEGER NOT NULL,
        "name"	TEXT NOT NULL,
        "email"	TEXT NOT NULL UNIQUE,
        "password_hash"	TEXT NOT NULL,
        PRIMARY KEY("id" AUTOINCREMENT)
    )'''
)

c.execute(
    '''CREATE TABLE "items" (
        "id"	INTEGER NOT NULL,
        "name"	TEXT NOT NULL UNIQUE,
        "description"	TEXT,
        "price" INTEGER NOT NULL,
        PRIMARY KEY("id" AUTOINCREMENT)
    )'''
)

c.execute(
    '''CREATE TABLE "templates" (
        "id"	INTEGER NOT NULL,
        "name"  TEXT NOT NULL,
        "description"	TEXT,
        PRIMARY KEY("id" AUTOINCREMENT)
    )'''
)

c.execute(
    '''CREATE TABLE tier_lists (
        user_id INTEGER,
        template_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (template_id) REFERENCES templates(id)
    )'''
)

c.execute(
    '''CREATE TABLE template_items (
        template_id INTEGER,
        item_id INTEGER,
        FOREIGN KEY (template_id) REFERENCES templates(id),
        FOREIGN KEY (item_id) REFERENCES items(id)
    )'''
)

c.execute(
    '''CREATE TABLE tier_list_items (
        tier_list_id INTEGER,
        item_id INTEGER,
        tier TEXT,
        FOREIGN KEY (item_id) REFERENCES items(id),
        FOREIGN KEY (tier_list_id) REFERENCES tier_lists(id),
        FOREIGN KEY (tier) REFERENCES tiers(tier)
    )'''
)

conn.commit()
