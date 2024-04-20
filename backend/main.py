from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

from backend.models.user import User

# https://github.com/pranjalpruthi/Streamlit-FastAPI/tree/main

SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
Base = declarative_base()

app = FastAPI()

@app.post("/users/", response_model=User)
def create_user(name: str, surname: str, email: str):
    with Session(engine) as session:
        user = User(name=name, surname=surname, email=email)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user