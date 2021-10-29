from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings import DB_FILE
from auth import user_model
from db import models


engine = create_engine(DB_FILE, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


user_model.Base.metadata.create_all(engine)
models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
