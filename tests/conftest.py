import httpx
import pytest
import sqlalchemy as sa
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from api.apps.auth.manager import password_helper
from api.apps.auth.models import User
from api.settings import settings

engine = sa.create_engine(settings.ALEMBIC_DB_URL, echo=True)
BASE_URL = "http://localhost:8000"
OWNER_EMAIL = "testowner@owner.ru"
OWNER_PASSWORD = "Password0987654321"


@pytest.fixture(scope="session")
def db_session() -> Session:
    with Session(engine) as session:
        yield session


@pytest.fixture(scope="session", autouse=True)
def client():
    with httpx.Client() as client:
        yield client


@pytest.fixture(scope="session", autouse=True)
def owner(db_session: Session):
    hashed_password = password_helper.hash(OWNER_PASSWORD)
    stmt = sa.insert(User).values(
        email=OWNER_EMAIL, hashed_password=hashed_password
    )

    try:
        db_session.execute(stmt)
        db_session.commit()
    except IntegrityError:
        print("Owner already exists")

    owner = {
        "email": OWNER_EMAIL,
        "password": OWNER_PASSWORD,
    }

    yield owner

    stmt = sa.delete(User).where(User.email == OWNER_EMAIL)

    try:
        db_session.execute(stmt)
        db_session.commit()
    except IntegrityError:
        print("Owner already deleted")
