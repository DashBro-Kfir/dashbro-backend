import bcrypt
from fastapi import HTTPException
from sqlmodel import Session, select

from dashbro.clients.db_client import DBClient
from dashbro.models.models import User
from logger import logger


class AuthService:
    def __init__(self, db_client: DBClient):
        self.db_client = db_client
        self.session: Session = self.db_client.get_session()
        logger.info("AuthService initialized with active DB session.")

    def signup_user(self, data):
        logger.info(f"Signup attempt for username: {data.username}")
        statement = select(User).where(User.username == data.username)
        result = self.session.exec(statement).first()

        if result:
            logger.warning(f"Signup failed: Username already exists - {data.username}")
            raise HTTPException(status_code=400, detail="Username already exists")

        hashed_pw = bcrypt.hashpw(data.password.encode(), bcrypt.gensalt()).decode()

        new_user = User(
            username=data.username, firstname=data.firstname, surname=data.surname, password=hashed_pw, email=data.email
        )
        self.session.add(new_user)
        self.session.commit()
        self.session.refresh(new_user)

        logger.info(f"User created successfully: {new_user.username}")
        return {"message": "User created successfully"}

    def login_user(self, data):
        logger.info(f"Login attempt for username: {data.username}")
        statement = select(User).where(User.username == data.username)
        user = self.session.exec(statement).first()

        if not user or not bcrypt.checkpw(data.password.encode(), user.password.encode()):
            logger.warning(f"Login failed for user: {data.username}")
            raise HTTPException(status_code=401, detail="Invalid credentials")

        logger.info(f"Login success for user: {data.username}")
        return {
            "id": user.id,
            "username": user.username,
            "firstname": user.firstname,
            "surname": user.surname,
            "email": user.email,
        }

    def close(self):
        if self.session:
            self.session.close()
            logger.info("AuthService DB session closed.")
