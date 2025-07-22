import bcrypt
from fastapi import HTTPException

from db_client import DBClient


def signup_user(data):
    db = DBClient()
    try:
        existing = db.execute("SELECT * FROM users WHERE username = %s", (data.username,), fetchone=True)
        if existing:
            raise HTTPException(status_code=400, detail="Username already exists")

        hashed_pw = bcrypt.hashpw(data.password.encode("utf-8"), bcrypt.gensalt()).decode()

        db.execute(
            """
            INSERT INTO users (username, firstname, surname, password, email)
            VALUES (%s, %s, %s, %s, %s)
        """,
            (data.username, data.firstname, data.surname, hashed_pw, data.email),
        )

        return {"message": "User created successfully"}

    finally:
        db.close()  # Always close


def login_user(data):
    db = DBClient()
    try:
        user = db.execute("SELECT * FROM users WHERE username = %s", (data.username,), fetchone=True)
        if not user or not bcrypt.checkpw(data.password.encode("utf-8"), user["password"].encode()):
            raise HTTPException(status_code=401, detail="Invalid credentials")

        return {
            "id": user["id"],
            "username": user["username"],
            "firstname": user["firstname"],
            "surname": user["surname"],
            "email": user["email"],
        }

    finally:
        db.close()  # Always close
