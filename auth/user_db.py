from fastapi import APIRouter, HTTPException, status
from fastapi.param_functions import Depends
from sqlalchemy.orm import Session
from auth.user_model import DbUser
from db_session import get_db


def get_user_by_username(username: str, db: Session = Depends(get_db)):
    user = db.query(DbUser).filter(DbUser.username == username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'User with username {username} not found'
        )
    return user
