from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from config import DATABASE_PATH

DATABASE_URL = DATABASE_PATH

engine = create_engine(DATABASE_URL)
session = Session(bind=engine)
