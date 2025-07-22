import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv
from logger import logger  

load_dotenv()

class DBClient:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT"),
                dbname=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD")
            )
            logger.info("Database connection established.")
        except Exception as e:
            logger.error(f"Failed to connect to the database: {e}")
            raise

    def execute(self, query, params=None, fetch=False, fetchone=False):
        try:
            with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
                logger.debug(f"Executing query: {query} | Params: {params}")
                cur.execute(query, params)
                if fetchone:
                    result = cur.fetchone()
                    logger.debug(f"Query result (one): {result}")
                    return result
                if fetch:
                    result = cur.fetchall()
                    logger.debug(f"Query result (all): {result}")
                    return result
                self.conn.commit()
                logger.debug("Query executed and committed successfully.")
        except Exception as e:
            logger.error(f"Error executing query: {e} | Query: {query} | Params: {params}")
            self.conn.rollback()
            raise

    def close(self):
        try:
            self.conn.close()
            logger.info("Database connection closed.")
        except Exception as e:
            logger.error(f"Error closing database connection: {e}")
