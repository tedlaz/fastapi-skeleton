from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from db.models import DbTrn, DbTrnd


def check_lines(lines):
    if len(lines) <= 1:
        raise ValueError("Transaction must have at least 2 lines")
    total = 0
    for line in lines:
        total += line.val
    if round(total, 2) != 0:
        raise ValueError("Transaction is not balanced")


def create(data, db):
    check_lines(data.lines)
    new_trn = DbTrn(
        date=data.date,
        seira=data.seira,
        pno=data.pno
    )

    for line in data.lines:
        new_trn.lines.append(DbTrnd(
            account=line.account,
            val=round(line.val, 2)
        ))

    try:
        db.add(new_trn)
        db.commit()
        db.refresh(new_trn)
    except IntegrityError:
        raise ValueError("Transaction already exists")
    return new_trn


def read_all(db: Session):
    return db.query(DbTrn).all()


def read_by_id(idv: int, db: Session):
    return db.query(DbTrn).filter(DbTrn.id == idv).first()


def update(idv: int, db: Session):
    trn = db.query(DbTrn).filter(DbTrn.id == idv).first()
    pass


def delete():
    pass
