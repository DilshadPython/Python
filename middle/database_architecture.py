"""
Section 13: Database Architecture & SQLAlchemy 2.0

Description: Master production database architecture: PostgreSQL SQL tuning, SQLAlchemy 2.0 ORM, Alembic migrations, connection pooling, and layer separation.
Level: Middle
URL: http://127.0.0.1:5000/python/middle/database_architecture
"""

# --- Code Snippet 1 ---
# ❌ Model does hashing, DB queries & email sending!
class User(Base):
    def register(self):
        self.password = hash_pwd(self.password)
        db.session.add(self)
        send_welcome_email(self.email)

# --- Code Snippet 2 ---
# ✅ Model = DB Entity | Schema = DTO | Repo = Queries | Service = Rules
class UserModel(Base): ...      # Entity
class UserCreate(BaseModel): ... # DTO
class UserRepository: ...       # SQL
class UserService: ...          # Logic

# --- Code Snippet 3 ---
# ─── 1. SQLALCHEMY 2.0 ORM ENTITY (models/user.py) ─────────────────────────
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String

class UserModel(DeclarativeBase):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)

# ─── 2. DATA ACCESS REPOSITORY (repositories/user_repo.py) ────────────────
from sqlalchemy import select

class UserRepository:
    def __init__(self, session): self.session = session

    def get_by_email(self, email: str) -> UserModel | None:
        stmt = select(UserModel).where(UserModel.email == email)
        return self.session.execute(stmt).scalars().first()

