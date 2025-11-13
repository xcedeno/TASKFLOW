from fastapi import FastAPI, Depends, HTTPException, status
from sqlmodel import Session
from app.database import init_db, engine, get_session
from app.models import User, Task, CalendarEvent
from app.schemas import UserCreate, TaskCreate, TaskRead, TaskUpdate, Token
from app.auth import get_password_hash, verify_password, create_access_token, get_user_by_email, oauth2_scheme, get_current_user
from app.crud import create_user, create_task, list_tasks, get_task, update_task, create_event
from fastapi.security import OAuth2PasswordRequestForm

app = FastAPI(title="TaskFlow IT")

@app.on_event("startup")
def on_startup():
    init_db()

# Auth endpoints
@app.post("/auth/register", response_model=dict)
def register(user: UserCreate):
    existing = get_user_by_email(user.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    u = User(email=user.email, full_name=user.full_name, hashed_password=get_password_hash(user.password))
    created = create_user(u)
    return {"msg":"user created", "id": created.id}

@app.post("/auth/token", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_user_by_email(form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token({"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

# Task endpoints
@app.post("/tasks", response_model=TaskRead)
def create_task_endpoint(task_in: TaskCreate, current_user: User = Depends(get_current_user)):
    task = Task(**task_in.dict())
    created = create_task(task)
    return created

@app.get("/tasks", response_model=list[TaskRead])
def list_tasks_endpoint(status: str = None, skip: int = 0, limit: int = 100, current_user: User = Depends(get_current_user)):
    return list_tasks(skip=skip, limit=limit, status=status)

@app.get("/tasks/{task_id}", response_model=TaskRead)
def get_task_endpoint(task_id: int, current_user: User = Depends(get_current_user)):
    task = get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.patch("/tasks/{task_id}", response_model=TaskRead)
def update_task_endpoint(task_id: int, payload: dict, current_user: User = Depends(get_current_user)):
    updated = update_task(task_id, payload)
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated

# Calendar event for a task
@app.post("/tasks/{task_id}/events")
def create_event_endpoint(task_id: int, event: dict, current_user: User = Depends(get_current_user)):
    # basic validation
    from datetime import datetime
    if not get_task(task_id):
        raise HTTPException(status_code=404, detail="Task not found")
    ev = CalendarEvent(task_id=task_id, title=event.get("title"), start=datetime.fromisoformat(event.get("start")), end=datetime.fromisoformat(event.get("end")), reminder_minutes=event.get("reminder_minutes"))
    created = create_event(ev)
    return {"id": created.id}
