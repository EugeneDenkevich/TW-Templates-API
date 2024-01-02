from typing import Final
from typing import final

from pydantic import StrictStr
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

from api import consts


@final
class Settings(BaseSettings):
    """
    App config.
    """

    model_config = SettingsConfigDict(
        case_sensitive=True,
        env_file_encoding="utf-8",
        env_file=consts.DIR_ROOT / ".env",
        env_prefix="WEBAPP_",
        extra="ignore",
        frozen=True,
    )

    APP_DB_URL: StrictStr
    ALEMBIC_DB_URL: StrictStr
    DB_NAME: StrictStr
    DB_USER: StrictStr
    DB_PASS: StrictStr
    TIME_TOKEN_EXPIRED: int
    SECRET_AUTH: StrictStr
    CORS_ALLOW_ORIGINS: StrictStr


settings: Final = Settings()


__all__ = ("settings",)
