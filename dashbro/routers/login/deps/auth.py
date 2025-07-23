from typing import Annotated

from fastapi import Depends

from dashbro.clients.db_client import DBClient
from dashbro.repositories.auth import AuthService
from dashbro.routers.login.deps.db import get_db_client


def get_auth_service(db_client: Annotated[DBClient, Depends(get_db_client)]):
    return AuthService(db_client)
