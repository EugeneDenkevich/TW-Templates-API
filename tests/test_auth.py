import httpx

from tests.conftest import BASE_URL
from tests.conftest import OWNER_EMAIL
from tests.conftest import OWNER_PASSWORD

BASE_URL = "http://localhost:8000"


def test_me_unauthorized():
    res = httpx.get(
        url=f"{BASE_URL}/users/me",
    )

    assert res.status_code == 401
    assert res.text == '{"detail":"Unauthorized"}'


def test_login():
    email = OWNER_EMAIL
    password = OWNER_PASSWORD

    res = httpx.post(
        url=f"{BASE_URL}/auth/login",
        data={"email": email, "password": password},
    )

    assert res.status_code == 204
    assert "ownertkn" in res.cookies
