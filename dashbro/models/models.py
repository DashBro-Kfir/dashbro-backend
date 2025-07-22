from typing import Optional

from pydantic import BaseModel, EmailStr
from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    firstname: str
    surname: str
    password: str  # This should be a hashed string
    email: str = Field(index=True, unique=True)


class SignupRequest(BaseModel):
    username: str
    firstname: str
    surname: str
    password: str
    email: EmailStr


class LoginRequest(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    firstname: str
    surname: str
    email: EmailStr
