from pydantic import BaseModel, EmailStr

class UserResponse(BaseModel):
    id: int
    username: str
    firstname: str
    surname: str
    email: EmailStr