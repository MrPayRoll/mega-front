from pydantic import BaseModel

class Task(BaseModel):
    task_name: str
    description: str
    img:str
    price:int
