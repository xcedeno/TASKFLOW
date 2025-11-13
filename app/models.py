from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from pydantic import EmailStr

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: EmailStr
    full_name: Optional[str]
    hashed_password: str
    is_active: bool = True
    is_admin: bool = False

class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: Optional[str] = None
    status: str = "todo"   # todo, in_progress, done, blocked
    priority: str = "medium"  # low, medium, high, urgent
    created_at: datetime = Field(default_factory=datetime.utcnow)
    due_date: Optional[datetime] = None
    assignee_id: Optional[int] = Field(default=None, foreign_key="user.id")
    assignee: Optional[User] = Relationship(back_populates="tasks")

User.tasks = Relationship(back_populates="assignee", sa_relationship_kwargs={"lazy":"selectin"})

class CalendarEvent(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    task_id: Optional[int] = Field(default=None, foreign_key="task.id")
    title: str
    start: datetime
    end: datetime
    reminder_minutes: Optional[int] = None
