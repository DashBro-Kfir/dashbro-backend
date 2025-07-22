from fastapi import FastAPI
from models import SignupRequest, LoginRequest, UserResponse
from auth import AuthService
from db_client import DBClient
from settings import settings

app = FastAPI()

user = "user"


# Initialize once
db_client = DBClient(
    settings.db_url
)
db_client.create_tables()
auth_service = AuthService(db_client)

@app.post("/signup")
def signup(req: SignupRequest):
    return auth_service.signup_user(req)

@app.post("/login", response_model=UserResponse)
def login(req: LoginRequest):
    return auth_service.login_user(req)

@app.on_event("shutdown")
def shutdown_event():
    auth_service.close()
