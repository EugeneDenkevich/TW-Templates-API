from fastapi import APIRouter
from fastapi import Depends

from api.apps.auth.base_config import current_user
from api.apps.auth.models import User
from api.apps.auth.schemas import UserRead

me_router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


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


__all__ = ("me_router",)
