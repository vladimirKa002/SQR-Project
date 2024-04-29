from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


engine = 0
db_session = 0


def setup_db(db_path):
    global engine, db_session
    engine = create_engine(db_path, connect_args={"check_same_thread": False})
    db_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    print("Creating db tables...")
    Base.metadata.create_all(bind=engine)
    inspection = inspect(engine)
    print(f"Created {len(inspection.get_table_names())} tables: {inspection.get_table_names()}")


class DBContext:

    def __init__(self):
        self.db = db_session()

    def __enter__(self):
        return self.db

    def __exit__(self, exc_type, exc_value, traceback):
        self.db.close()


def get_db():
    """ Returns the current db connection """
    with DBContext() as db:
        yield db
