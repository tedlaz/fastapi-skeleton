from fastapi import FastAPI
from auth import auth_router, user_model, user_router
from db_session import engine
from db import models
from routers import trn_router, acc_router


app = FastAPI()

for rout in (auth_router, user_router, trn_router, acc_router):
    app.include_router(rout.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


user_model.Base.metadata.create_all(engine)
models.Base.metadata.create_all(engine)
