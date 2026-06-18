from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories import user_repository
from app.schemas.user_schema import UserCreate


def create_user(db: Session, user_data: UserCreate):
    user_already_exists = user_repository.get_user_by_email(
        db=db,
        email=user_data.email
    )

    if user_already_exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    return user_repository.create_user(db=db, user_data=user_data)


def get_users(db: Session):
    return user_repository.get_users(db=db)


def get_user_by_id(db: Session, user_id: int):
    user = user_repository.get_user_by_id(db=db, user_id=user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return user