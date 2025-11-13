from sqlmodel import SQLModel, create_engine, Session
from .config import settings
from sqlalchemy.engine.url import make_url

DATABASE_URL = settings.DATABASE_URL
engine = create_engine(DATABASE_URL, echo=False)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
