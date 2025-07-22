from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # logger
    logs_directory: str = "logs/app.log"
    app_name: str = "dashbro"

    #DB
    db_url = "postgresql://db_user:pass123@localhost:5432/db_name"



settings = Settings()
