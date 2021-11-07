# from schemas import UserBase, UserDisplay
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from auth.user_model import DbUser
from auth import hash
from auth.user_schemas import UserBase, UserDisplay
from db_session import get_db


router = APIRouter(prefix='/user', tags=['user'])


@router.post('/', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    new_user = DbUser(
        username=request.username,
        email=request.email,
        password=hash.encrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get('/', response_model=list[UserDisplay])
def get_all_users(db: Session = Depends(get_db)):
    return db.query(DbUser).all()


@router.get('/{username}', response_model=UserDisplay)
def get_user(username: str, db: Session = Depends(get_db)):
    return db.query(DbUser).filter(DbUser.username == username).first()


@router.post('/{id}', response_model=UserDisplay)
def update_user(id: int, request: UserBase, db: Session = Depends(get_db)):
    user = db.query(DbUser).filter(DbUser.id == id)
    user.update({
        DbUser.username: request.username,
        DbUser.email: request.email,
        DbUser.password: hash.encrypt(request.password)
    })
    db.commit()
    return user.first()
