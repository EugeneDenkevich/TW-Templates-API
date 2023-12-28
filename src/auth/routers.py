from fastapi import APIRouter, Depends
from src.auth.base_config import current_user

from src.auth.models import User
from src.auth.schemas import UserRead

me_router = APIRouter()

@me_router.get("/me", response_model=UserRead)
async def me(user: User = Depends(current_user)):
    return {
            "id": user.id,
            "email": user.email,
            "is_active": user.is_active,
            "is_superuser": user.is_superuser,
            "is_verified": user.is_verified,
        }