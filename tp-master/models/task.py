from sqlalchemy import Column,Integer,String,ForeignKey
from db import Base

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    task_name = Column(String, nullable=False, index=True)
    description = Column(String, nullable=False)
    img = Column(String,nullable=False)
    price = Column(String,nullable=False)
