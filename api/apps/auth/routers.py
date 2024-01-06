from fastapi import APIRouter
from fastapi import Depends

from api.apps.auth.base_config import auth_backend
from api.apps.auth.base_config import current_user
from api.apps.auth.base_config import fastapi_users
from api.apps.auth.models import User
from api.apps.auth.schemas import UserCreate
from api.apps.auth.schemas import UserRead

auth_router = APIRouter(prefix="/auth")
me_router = APIRouter(prefix="/auth")

auth_router.include_router(fastapi_users.get_auth_router(auth_backend))
auth_router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate)
)


@me_router.get("/me", response_model=UserRead)
async def get_me(user: User = Depends(current_user)):
    return user


auth_routers = (
    auth_router,
    me_router,
)


__all__ = ("auth_routers",)
