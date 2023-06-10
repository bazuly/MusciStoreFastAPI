from fastapi import FastAPI
from fastapi_users import FastAPIUsers
from auth.auth_cookie import auth_backend
from auth.auth_user_manager import get_user_manager
from auth.auth_user_shemas import UserRead, UserCreate
from auth.auth_database import *
from routers.router import router as router_exchange


app = FastAPI(
    title='Music instruments exchange'
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(router_exchange)

