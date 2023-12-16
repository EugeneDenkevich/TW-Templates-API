from fastapi_users import FastAPIUsers
from fastapi_users import models
from fastapi_users.authentication import AuthenticationBackend
from fastapi_users.authentication import CookieTransport
from fastapi_users.authentication import JWTStrategy
from fastapi_users.jwt import generate_jwt
from sqlalchemy import select

from src.auth.manager import get_user_manager
from src.auth.models import User
from src.auth.models import role
from src.config import SECRET_AUTH
from src.config import TIME_TOKEN_EXPIRED
from src.database import AsyncSession
from src.database import get_async_session

cookie_transport = CookieTransport(
    cookie_name="ownertkn", cookie_max_age=TIME_TOKEN_EXPIRED
)


class TemplateJWTStrategy(JWTStrategy):
    async def get_user_role(self, user):
        stmt = select(role).where(role.c.id == user.role_id)
        session: AsyncSession = [
            session async for session in get_async_session()
        ][0]
        user_roles = await session.execute(stmt)

        # fixme
        # TODO
        # - make correct role processing
        user_role = user_roles.first()
        if user_role:
            return str(user_role.name)
        return "unknown_role"

    async def write_token(self, user: models.UP) -> str:
        user_role = await self.get_user_role(user)
        data = {
            "sub": str(user.id),
            "role": user_role,
            "aud": self.token_audience,
        }
        return generate_jwt(
            data,
            self.encode_key,
            self.lifetime_seconds,
            algorithm=self.algorithm,
        )


def get_jwt_strategy() -> TemplateJWTStrategy:
    return TemplateJWTStrategy(secret=SECRET_AUTH, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user(active=True)
