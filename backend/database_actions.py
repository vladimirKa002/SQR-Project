from typing import Optional

from schemas import UserCreate
from database import DBContext
from models import User
from security import hash_password, manager
from sqlalchemy.orm import Session


@manager.user_loader()
def get_user(email: str, db: Session = None) -> Optional[User]:
    """Return the user with the corresponding email"""
    if db is None:
        with DBContext() as db:
            return db.query(User).filter(User.email == email).first()
    else:
        return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user: UserCreate) -> User:
    """Create a new entry in the database user table"""
    user_data = user.dict()
    user_data["password"] = hash_password(user.password)
    db_user = User(**user_data)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
