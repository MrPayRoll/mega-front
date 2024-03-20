from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import getdb
from services import task as task_service
from dto.task import Task

router = APIRouter()

@router.get("/tasks", response_model=List[Task], tags=['tasks'])
async def get_tasks(db: Session = Depends(getdb)):
    return task_service.get_tasks(db)

@router.get("/tasks/{id}", response_model=Task, tags=['tasks'])
async def get_task(id: int, db: Session = Depends(getdb)):
    return task_service.get_task(id, db)

@router.post("/tasks", response_model=Task, tags=['tasks'])
async def create_task(data: Task, db: Session = Depends(getdb)):
    return task_service.create_task(data, db)

@router.delete("/tasks/{id}", tags=['tasks'])
async def delete_task(id: int, db: Session = Depends(getdb)):
    return task_service.delete_task(id, db)

@router.put("/tasks/{task_id}/register/{user_id}", tags=['tasks'])
async def register_task(task_id: int, user_id: int, db: Session = Depends(getdb)):
    return task_service.sign_up_for_task(user_id, task_id, db)
