"""
Section 6: The Repository Pattern & Data Access Decoupling

Description: Master the Repository Pattern in Python: decouple business logic from SQLAlchemy ORM, define abstract repository contracts, and enable in-memory unit testing.
Level: Middle
URL: http://127.0.0.1:5000/python/middle/repository_pattern
"""

# --- Code Snippet 1 ---
# ❌ Tight coupling to ORM and Database driver
@app.route("/users/")
def get_user(user_id):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        abort(404)
    return jsonify(user.to_dict())

# --- Code Snippet 2 ---
# ✅ Clean domain service calling abstract repository
class UserService:
    def __init__(self, user_repo: UserRepository) -> None:
        self.user_repo = user_repo

    def get_user_profile(self, user_id: int) -> User:
        user = self.user_repo.get_by_id(user_id)
        return user

# --- Code Snippet 3 ---
# ─── 1. ABSTRACT REPOSITORY CONTRACT ──────────────────────────────────────
from abc import ABC, abstractmethod
from typing import Optional

class UserRepository(ABC):
    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[User]:
        ...

# ─── 2. PRODUCTION SQLALCHEMY IMPLEMENTATION ──────────────────────────────
class SqlAlchemyUserRepository(UserRepository):
    def __init__(self, db_session) -> None:
        self.session = db_session

    def get_by_id(self, user_id: int) -> Optional[User]:
        orm_user = self.session.query(UserModel).filter(UserModel.id == user_id).first()
        return User(id=orm_user.id, email=orm_user.email) if orm_user else None

# ─── 3. IN-MEMORY MOCK REPOSITORY (FOR LIGHTNING UNIT TESTS) ──────────────
class InMemoryUserRepository(UserRepository):
    def __init__(self) -> None:
        self._users: dict[int, User] = {}

    def get_by_id(self, user_id: int) -> Optional[User]:
        return self._users.get(user_id)

