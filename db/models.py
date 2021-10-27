from enum import unique
from sqlalchemy import Column, ForeignKey, PrimaryKeyConstraint, UniqueConstraint
from sqlalchemy.sql.sqltypes import Integer, String, Date, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class DbAccount(Base):
    __tablename__ = 'acc'

    code = Column(String, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)


class DbCounterPart(Base):
    __tablename__ = 'cpart'

    afm = Column(String, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=True)
    branch = Column(Integer)
    country = Column(String)
    city = Column(String)
    post_code = Column(String)


class DbTrn(Base):
    __tablename__ = 'trn'

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    seira = Column(String)
    pno = Column(String)

    lines = relationship('DbTrnd', back_populates='tran')
    UniqueConstraint(date, seira, pno)


class DbTrnd(Base):
    __tablename__ = 'trnd'

    id = Column(Integer, primary_key=True, index=True)
    tran_id = Column(Integer, ForeignKey('trn.id'))
    account = Column(String)
    val = Column(Numeric)

    tran = relationship('DbTrn', back_populates='lines')
