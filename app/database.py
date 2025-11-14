from sqlmodel import SQLModel, create_engine, Session
from .config import settings
import time
import logging
from sqlalchemy.exc import OperationalError

logger = logging.getLogger(__name__)

DATABASE_URL = settings.DATABASE_URL
engine = create_engine(DATABASE_URL, echo=False)


def init_db(retries: int = 8, base_delay: float = 1.0):
    """Initialize the database schema, waiting for the DB to be available.

    This will attempt to connect to the database up to `retries` times using
    exponential backoff starting at `base_delay` seconds. If the database is
    reachable the metadata is created. If not reachable after retries, an
    exception is raised to fail startup intentionally.
    """
    attempt = 0
    while attempt < retries:
        try:
            # try acquiring a connection (this will raise OperationalError if DB isn't ready)
            with engine.connect() as conn:
                logger.info("Database connection established on attempt %d", attempt + 1)
                break
        except OperationalError as exc:
            attempt += 1
            wait = base_delay * (2 ** (attempt - 1))
            logger.warning("Database unavailable (attempt %d/%d): %s. Retrying in %.1f seconds...",
                        attempt, retries, str(exc).splitlines()[0], wait)
            time.sleep(wait)
    else:
        # If we exit the loop without break, DB never became available
        raise RuntimeError(f"Could not connect to the database after {retries} attempts")

    # Create tables once the DB is reachable
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
