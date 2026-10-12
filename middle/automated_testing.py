"""
Section 10: Automated Testing & Test Pyramid Strategy

Description: Master automated testing in Python with pytest: unit, integration, and API testing, fixtures, parametrization, mocking, and coverage.
Level: Middle
URL: http://127.0.0.1:5000/python/middle/automated_testing
"""

# --- Code Snippet 1 ---
# ✅ Runs 50 tests in < 1 second via pytest
def test_create_user_api_success(client):
    res = client.post("/users", json={"email": "test@dev.com", "password": "Pass!"})
    assert res.status_code == 201
    assert res.json()["email"] == "test@dev.com"

# --- Code Snippet 2 ---
# ─── 1. SHARED TEST FIXTURES (tests/conftest.py) ──────────────────────────
import pytest
from fastapi.testclient import TestClient

@pytest.fixture
def mock_repo():
    return InMemoryUserRepository()

@pytest.fixture
def client(mock_repo):
    app.dependency_overrides[get_user_repo] = lambda: mock_repo
    with TestClient(app) as c:
        yield c

# ─── 2. PARAMETRIZED UNIT TEST (tests/unit/test_users.py) ──────────────────
@pytest.mark.parametrize("pwd, is_valid", [
    ("short", False),
    ("ValidSecret123!", True),
])
def test_password_validation(pwd: str, is_valid: bool):
    assert validate_password(pwd) == is_valid

