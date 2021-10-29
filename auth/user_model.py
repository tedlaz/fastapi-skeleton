from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import event, DDL
from auth.hash import Hash

Base = declarative_base()


class DbUser(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String)
    password = Column(String)


event.listen(
    DbUser.__table__,
    'after_create',
    DDL(
        (
            "INSERT INTO users (id, username, email, password) VALUES"
            f" (1, 'ted', 'ted@gmail.com', '{Hash.encrypt('123')}')"
        )
    )
)
