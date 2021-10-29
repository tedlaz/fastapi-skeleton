from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from db.models import DbTrn, DbTrnd
from auth.oauth2 import get_current_user
from auth.user_schemas import UserBase
from schemas.trn_schemas import TrnNew, TrnDisplay
from db_session import get_db


def check_lines_and_raise_exceptions(lines):
    if len(lines) <= 1:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Transaction must have at least 2 lines"
        )
    total = 0
    for line in lines:
        total += line.val
    if round(total, 2) != 0:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Transaction is not balanced"
        )


router = APIRouter(prefix='/trn', tags=['trn'])


@router.post('/', response_model=TrnDisplay)
async def create_trn(request: TrnNew, db: Session = Depends(get_db), _: UserBase = Depends(get_current_user)):
    check_lines_and_raise_exceptions(request.lines)
    new_trn = DbTrn(
        date=request.date,
        seira=request.seira,
        pno=request.pno
    )

    for line in request.lines:
        new_trn.lines.append(DbTrnd(
            account=line.account,
            val=round(line.val, 2)
        ))

    try:
        db.add(new_trn)
        db.commit()
        db.refresh(new_trn)
    except IntegrityError:
        raise HTTPException(
            status_code=404, detail="Transaction already exists")
    return new_trn


@router.get('/', response_model=list[TrnDisplay])
async def get_all_transactions(db: Session = Depends(get_db), _: UserBase = Depends(get_current_user)):
    return db.query(DbTrn).all()
