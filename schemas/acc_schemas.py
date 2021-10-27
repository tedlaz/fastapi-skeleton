from pydantic import BaseModel


class AccNew(BaseModel):
    code: str
    name: str


class AccDisplay(BaseModel):
    code: str
    name: str

    class Config():
        orm_mode = True
