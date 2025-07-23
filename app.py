import uvicorn
from fastapi import FastAPI

from dashbro.routers.base import base_router
from settings import settings

app = FastAPI()
app.include_router(base_router)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)
