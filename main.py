from fastapi import FastAPI
from auth import auth_router, user_router
from routes import main_router, trn_router, acc_router


app = FastAPI()

trout = (
    main_router,
    auth_router,
    user_router,
    trn_router,
    acc_router
)

for rout in trout:
    app.include_router(rout.router)
