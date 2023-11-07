from datetime import datetime

from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Quest(Base):

    __tablename__ = 'quest'

    id = Column(Integer, primary_key=True)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    added_at = Column(TIMESTAMP, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.question} / {self.answer} / {self.created_at}"
