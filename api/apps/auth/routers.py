from fastapi import APIRouter
from fastapi import Depends

from api.apps.auth.auth import get_auth_router
from api.apps.auth.base_config import current_user
from api.apps.auth.base_config import fastapi_users
from api.apps.auth.models import User
from api.apps.auth.schemas import UserCreate
from api.apps.auth.schemas import UserRead
from api.settings import settings

auth_router = APIRouter(prefix="/auth", tags=["Auth"])
me_router = APIRouter(prefix="/users", tags=["Users"])


auth_router.include_router(get_auth_router())


@me_router.get("/me", response_model=UserRead)
async def get_me(user: User = Depends(current_user)):
    return user


if settings.DEBUG is True:
    auth_router.include_router(
        fastapi_users.get_register_router(UserRead, UserCreate)
    )



routers = (
    auth_router,
    me_router,
)


__all__ = ("routers",)
