from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.models import DbAccount
from auth.oauth2 import get_current_user
from auth.user_schemas import UserBase
from schemas.acc_schemas import AccNew, AccDisplay
from db_session import get_db


router = APIRouter(prefix='/account', tags=['account'])


@router.post('/', response_model=AccDisplay)
async def create_account(request: AccNew, db: Session = Depends(get_db), _: UserBase = Depends(get_current_user)):
    new_account = DbAccount(
        code=request.code,
        name=request.name
    )
    db.add(new_account)
    db.commit()
    db.refresh(new_account)
    return new_account


@router.get('/', response_model=list[AccDisplay])
async def get_all_accounts(db: Session = Depends(get_db), _: UserBase = Depends(get_current_user)):
    return db.query(DbAccount).all()
