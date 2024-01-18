from typing import Optional
from typing import final

from fastapi_users import schemas
from pydantic import BaseModel
from pydantic import StrictStr


@final
class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        orm_mode = True


@final
class UserCreate(schemas.BaseUserCreate):
    email: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


@final
class ChangePassword(BaseModel):
    current_password: StrictStr
    new_password: StrictStr
    new_password_confirm: StrictStr
