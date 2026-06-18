from datetime import datetime, UTC

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.enums import TaskStatus
from app.repositories import task_repository, user_repository
from app.schemas.task_schema import TaskCreate, TaskUpdate


def create_task(db: Session, task_data: TaskCreate):
    user = user_repository.get_user_by_id(
        db=db,
        user_id=task_data.user_id
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return task_repository.create_task(
        db=db,
        task_data=task_data
    )


def get_tasks(db: Session):
    return task_repository.get_tasks(db=db)


def get_task_by_id(db: Session, task_id: int):
    task = task_repository.get_task_by_id(
        db=db,
        task_id=task_id
    )

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    return task


def update_task(
    db: Session,
    task_id: int,
    task_data: TaskUpdate
):
    task = get_task_by_id(
        db=db,
        task_id=task_id
    )

    if task_data.status == TaskStatus.COMPLETED:
        task.completed_at = datetime.now(UTC)

    return task_repository.update_task(
        db=db,
        task=task,
        task_data=task_data
    )


def delete_task(
    db: Session,
    task_id: int
):
    task = get_task_by_id(
        db=db,
        task_id=task_id
    )

    task_repository.delete_task(
        db=db,
        task=task
    )