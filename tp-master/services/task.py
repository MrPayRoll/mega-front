from sqlalchemy.orm import Session
from models.task import Task
from dto.task import Task as TaskDto
from models.user import User
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

def create_task(data: TaskDto, db: Session):
    task = Task(**data.dict())
    try:
        db.add(task)
        db.commit()
        db.refresh(task)
        return task
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Task creation failed")

def get_tasks(db: Session):
    return db.query(Task).all()

def get_task(id: int, db: Session):
    return db.query(Task).filter(Task.id == id).first()

def delete_task(id: int, db: Session):
    task = db.query(Task).filter(Task.id == id).first()
    if task:
        db.delete(task)
        db.commit()
        return task
    else:
        raise HTTPException(status_code=404, detail="Task not found")

def sign_up_for_task(user_id: int, task_id: int, db: Session):
    try:
        user = db.query(User).filter(User.id == user_id).first()
        task = db.query(Task).filter(Task.id == task_id).first()

        if user is None or task is None:
            raise HTTPException(status_code=404, detail="User or task not found")

        if task.members is None:
            task.members = [user_id]
        else:
            task.members.append(user_id)

        db.commit()
        return {"message": f"User '{user.login}' successfully signed up for task '{task.task_name}'."}

    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="User is already signed up for this task")
