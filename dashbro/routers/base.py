from fastapi import APIRouter
from routers.login.login import login_router
from settings import settings

base_router = APIRouter()

@base_router.get("/")
def get_home():
    return ""

base_router.include_router(login_router)