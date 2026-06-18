from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app.enums import TaskPriority, TaskStatus


class TaskBase(BaseModel):
    title: str
    details: Optional[str] = None
    status: TaskStatus = TaskStatus.PENDING
    priority: TaskPriority = TaskPriority.MEDIUM
    category: Optional[str] = None
    estimated_time: Optional[str] = None
    due_date: Optional[datetime] = None


class TaskCreate(TaskBase):
    user_id: int


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    details: Optional[str] = None
    status: Optional[TaskStatus] = None
    priority: Optional[TaskPriority] = None
    category: Optional[str] = None
    estimated_time: Optional[str] = None
    due_date: Optional[datetime] = None


class TaskResponse(TaskBase):
    id: int
    user_id: int
    completed_at: Optional[datetime] = None
    reminder_sent_at: Optional[datetime] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True