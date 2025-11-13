from sqlmodel import select
from .models import Task, User, CalendarEvent
from sqlmodel import Session
from .database import engine

def create_user(data):
    with Session(engine) as s:
        s.add(data)
        s.commit()
        s.refresh(data)
        return data

def create_task(task: Task):
    with Session(engine) as s:
        s.add(task)
        s.commit()
        s.refresh(task)
        return task

def get_task(task_id: int):
    with Session(engine) as s:
        return s.get(Task, task_id)

def list_tasks(skip: int = 0, limit: int = 100, status: str = None):
    with Session(engine) as s:
        q = select(Task)
        if status:
            q = q.where(Task.status == status)
        return s.exec(q.offset(skip).limit(limit)).all()

def update_task(task_id: int, values: dict):
    with Session(engine) as s:
        task = s.get(Task, task_id)
        if not task:
            return None
        for k, v in values.items():
            setattr(task, k, v)
        s.add(task)
        s.commit()
        s.refresh(task)
        return task

def create_event(event: CalendarEvent):
    with Session(engine) as s:
        s.add(event)
        s.commit()
        s.refresh(event)
        return event
