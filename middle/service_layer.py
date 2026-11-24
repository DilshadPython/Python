"""
Section 7: The Service Layer & Orchestration Boundaries

Description: Master the Service Layer pattern in Python: separate HTTP routers from domain services, eliminate fat controllers, and orchestrate validation and security logic.
Level: Middle
URL: http://127.0.0.1:5000/python/middle/service_layer
"""

# --- Code Snippet 1 ---
# ❌ Route handles validation, hashing, SQL, and email
@router.post("/users")
def create_user(data: UserCreate):
    # 20 lines of email validation
    # 15 lines of password policy checks
    # 10 lines of bcrypt hashing
    # 25 lines of raw SQL insert queries
    # 30 lines of SMTP email dispatch...
    return {"status": "ok"}

# --- Code Snippet 2 ---
# ✅ Route delegates 100% of work to UserService
@router.post("/users", status_code=201)
def create_user(data: UserCreate, service: UserService = Depends()):
    return service.create_user(data)

class UserService:
    def create_user(self, data: UserCreate):
        validate_user(data)
        password = hash_password(data.password)
        return self.user_repo.create(data.email, password)

# --- Code Snippet 3 ---
# ─── 1. HTTP ROUTER (API DELIVERY LAYER) ───────────────────────────────────
@router.post("/users", status_code=201)
def create_user_endpoint(data: UserCreate, service: UserService = Depends()):
    return service.create_user(data)

# ─── 2. DOMAIN SERVICE (WORKFLOW ORCHESTRATION) ────────────────────────────
class UserService:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repo = user_repository

    def create_user(self, data: UserCreate) -> User:
        # Step 1: Validate email uniqueness constraint
        if self.user_repo.get_by_email(data.email):
            raise ValueError(f"Email '{data.email}' is already registered.")

        # Step 2: Perform password hashing transformation
        hashed_pwd = hash_password(data.password)

        # Step 3: Delegate entity creation to Repository contract
        return self.user_repo.create(
            email=data.email,
            hashed_password=hashed_pwd
        )

