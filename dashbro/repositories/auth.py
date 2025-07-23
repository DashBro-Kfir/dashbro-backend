import bcrypt
from fastapi import HTTPException
from sqlmodel import Session, select

from dashbro.schemas.login_request import SignupRequest
from dashbro.schemas.login_request import LoginRequest

from dashbro.clients.db_client import DBClient
from dashbro.models.user import User
from logger import logger


class AuthService:
    def __init__(self, db_client: DBClient):
        self.db_client = db_client
        self.session: Session = self.db_client.get_session()
        logger.info("AuthService initialized with active DB session.")

    def signup_user(self, login_request: SignupRequest):
        logger.info(f"Signup attempt for username: {login_request.username}")
        statement = select(User).where(User.username == login_request.username)
        result = self.session.exec(statement).first()

        if result:
            logger.warning(f"Signup failed: Username already exists - {login_request.username}")
            raise HTTPException(status_code=400, detail="Username already exists")

        hashed_pw = bcrypt.hashpw(login_request.password.encode(), bcrypt.gensalt()).decode()

        new_user = User(
            username=login_request.username, firstname=login_request.firstname, surname=login_request.surname, password=hashed_pw, email=login_request.email
        )
        self.session.add(new_user)
        self.session.commit()
        self.session.refresh(new_user)

        logger.info(f"User created successfully: {new_user.username}")
        return {"message": "User created successfully"}

    def login_user(self, login_request: LoginRequest):
        logger.info(f"Login attempt for username: {login_request.username}")
        statement = select(User).where(User.username == login_request.username)
        user = self.session.exec(statement).first()

        if not user or not bcrypt.checkpw(login_request.password.encode(), user.password.encode()):
            logger.warning(f"Login failed for user: {login_request.username}")
            raise HTTPException(status_code=401, detail="Invalid credentials")

        logger.info(f"Login success for user: {login_request.username}")
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
