from sqlmodel import SQLModel, Session, create_engine
from sqlalchemy.exc import SQLAlchemyError
from logger import logger


class DBClient:
    def __init__(self, database_url):
        try:
            self.database_url = database_url
            self.engine = create_engine(self.database_url, echo=False)
            logger.info("SQLModel engine created.")
        except Exception as e:
            logger.error(f"Failed to create SQLModel engine: {e}")
            raise

    def create_tables(self):
        try:
            SQLModel.metadata.create_all(self.engine)
            logger.info("All tables created successfully.")
        except Exception as e:
            logger.error(f"Failed to create tables: {e}")
            raise

    def get_session(self):
        try:
            return Session(self.engine)
        except SQLAlchemyError as e:
            logger.error(f"Failed to create DB session: {e}")
            raise
