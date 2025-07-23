from fastapi import Depends
from dashbro.repositories.auth import AuthService
from dashbro.routers.login.deps.db import get_db_client

def get_auth_service(db_client=Depends(get_db_client)):
    return AuthService(db_client)
