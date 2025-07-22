from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # logger
    logs_directory: str = "logs/app.log"
    app_name: str = "dashbro"


settings = Settings()
