from sqlalchemy import Column, Integer, String
from db import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    login = Column(String, unique=True, index=True)
    password = Column(String, unique=False, index=True)
    role = Column(String, unique=False, index=True)
