from fastapi import APIRouter

from dashbro.clients.db_client import DBClient
from dashbro.models.models import LoginRequest, SignupRequest, UserResponse
from dashbro.repositories.auth import AuthService
from settings import settings

base_router = APIRouter()

# Initialize once
db_client = DBClient(settings.db_url)
db_client.create_tables()
auth_service = AuthService(db_client)


@base_router.post("/signup")
def signup(req: SignupRequest):
    return auth_service.signup_user(req)


@base_router.post("/login", response_model=UserResponse)
def login(req: LoginRequest):
    return auth_service.login_user(req)
