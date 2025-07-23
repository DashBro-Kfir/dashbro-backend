from sqlalchemy.exc import SQLAlchemyError
from sqlmodel import Session, SQLModel, create_engine

from logger import logger


class DBClient:
    def __init__(self, database_url):
        try:
            self.database_url = database_url
            self.engine = create_engine(self.database_url, echo=False)
            logger.info("SQLModel engine created.")
            SQLModel.metadata.create_all(self.engine)
        except Exception as e:
            logger.error(f"Failed to create SQLModel engine: {e}")
            raise

    def get_session(self):
        try:
            return Session(self.engine)
        except SQLAlchemyError as e:
            logger.exception(f"Failed to create DB session: {e}")
            raise
