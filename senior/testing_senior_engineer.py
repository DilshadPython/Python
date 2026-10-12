"""
Track 06: Testing Like a Senior Engineer

Description: Master Senior Python Track 06: Advanced Testing Architecture. Fixture scopes, transaction rollback isolation, Fakes over fragile Mocks, and Property-Based Testing with Hypothesis.
Level: Senior
URL: http://127.0.0.1:5000/python/senior/testing_senior_engineer
"""

# --- Code Snippet 1 ---
import pytest

@pytest.fixture
def db_transaction(db_session):
    """Function-scoped transaction rollback fixture."""
    connection = db_session.engine.connect()
    transaction = connection.begin()
    
    yield connection
    
    # Instant rollback avoids expensive table truncation or recreating schemas
    transaction.rollback()
    connection.close()

@pytest.mark.parametrize("role,expected_access", [
    ("admin", True),
    ("developer", True),
    ("guest", False),
])
def test_role_access_matrix(role: str, expected_access: bool):
    assert check_access(role) == expected_access

# --- Code Snippet 2 ---
class InMemoryUserRepository:
    """Fake repository preserving interface contract in RAM."""
    def __init__(self):
        self._store: dict[str, dict] = {}

    def save(self, user_id: str, data: dict) -> None:
        self._store[user_id] = data

    def get_by_id(self, user_id: str) -> dict | None:
        return self._store.get(user_id)

def test_user_onboarding():
    repo = InMemoryUserRepository()
    service = UserService(repo)
    
    user = service.register_user("u1", "alex@cloud.dev")
    assert repo.get_by_id("u1")["email"] == "alex@cloud.dev"

# --- Code Snippet 3 ---
from hypothesis import given, strategies as st

def quicksort(arr: list[int]) -> list[int]:
    if len(arr)  pivot]
    return quicksort(left) + middle + quicksort(right)

@given(st.lists(st.integers()))
def test_sorting_preserves_length_and_order(xs: list[int]):
    sorted_xs = quicksort(xs)
    assert len(sorted_xs) == len(xs)
    assert all(sorted_xs[i] <= sorted_xs[i + 1] for i in range(len(sorted_xs) - 1))

