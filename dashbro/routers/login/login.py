from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query

from dashbro.clients.db_client import DBClient
from dashbro.repositories.auth import AuthService
from dashbro.routers.login.deps.auth import get_auth_service
from dashbro.schemas.login_request import LoginRequest
from dashbro.schemas.signup_request import SignupRequest
from dashbro.schemas.user_response import UserResponse
from settings import settings

# Initialize once
db_client = DBClient(settings.db_url)
auth_service = AuthService(db_client)

login_router = APIRouter(prefix="/")


@login_router.post("/signup")
def signup(signup_request: SignupRequest, auth_service: Annotated[AuthService, Depends(get_auth_service)]):
    return auth_service.signup(signup_request)


@login_router.post("/login")
def login(login_request: LoginRequest, auth_service: Annotated[AuthService, Depends(get_auth_service)]):
    return auth_service.login(login_request)
