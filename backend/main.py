import sqlite3
import bcrypt

from fastapi import FastAPI, HTTPException
from backend.database.database import conn, c
from backend.models.user import User

app = FastAPI()


@app.post("/user/register")
def register_user(user: User):
    hashed_password = bcrypt.hash(user.password)
    try:
        # Insert the user into the database
        c.execute("INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)",
                  (user.username, user.email, hashed_password))
        conn.commit()
        return {"message": "User registered successfully"}
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="Username or email already exists")


@app.post("/user/login")
def login_user(user: User):
    # Check if the user exists in the database
    c.execute("SELECT * FROM users WHERE email = ?", user.email)
    stored_user = c.fetchone()

    if stored_user is None:
        raise HTTPException(status_code=401, detail="User does not exist")

    # Verify the password
    if not bcrypt.verify(user.password_hash, stored_user[2]):
        raise HTTPException(status_code=401, detail="Incorrect username or password")

    return {"message": "Login successful", "user_id": stored_user[0]}
