from fastapi import APIRouter
from fastapi import Depends

from api.apps.auth.base_config import auth_backend
from api.apps.auth.base_config import current_user
from api.apps.auth.base_config import fastapi_users
from api.apps.auth.models import User
from api.apps.auth.schemas import UserCreate
from api.apps.auth.schemas import UserRead

auth_router = fastapi_users.get_auth_router(auth_backend)
register_router = fastapi_users.get_register_router(UserRead, UserCreate)
me_router = APIRouter()


@me_router.get("/me", response_model=UserRead)
async def me(user: User = Depends(current_user)):
    data = {
        "id": user.id,
        "email": user.email,
        "is_active": user.is_active,
        "is_superuser": user.is_superuser,
        "is_verified": user.is_verified,
    }
    return data


auth_routers = (
    auth_router,
    register_router,
    me_router,
)


__all__ = ("auth_routers",)
