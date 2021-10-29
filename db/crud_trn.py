from sqlalchemy.orm import Session
from db.models import DbTrn, DbTrnd


def create():
    pass


def read_all(db: Session):
    return db.query(DbTrn).all()


def read_by_id(idv: int, db: Session):
    return db.query(DbTrn).filter(DbTrn.id == idv).first()


def update():
    pass


def delete():
    pass
