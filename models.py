from pydantic import BaseModel, EmailStr


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
