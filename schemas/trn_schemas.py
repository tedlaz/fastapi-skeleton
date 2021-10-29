from datetime import date
from pydantic import BaseModel


class TrndList(BaseModel):
    account: str
    val: float


class TrnNew(BaseModel):
    date: date
    seira: str
    pno: str
    lines: list[TrndList]


class TrndDisplay(BaseModel):
    id: int
    account: str
    val: float

    class Config():
        orm_mode = True


class TrnDisplay(BaseModel):
    id: int
    date: date
    seira: str
    pno: str
    lines: list[TrndDisplay]

    class Config():
        orm_mode = True
