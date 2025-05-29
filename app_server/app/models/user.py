from sqlalchemy import Column, Integer, String, Date
from app.db.sqlite import Base

class User(Base):
    __tablename__ = "users"

    guid = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    birthday = Column(Date, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)