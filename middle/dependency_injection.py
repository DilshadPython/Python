"""
Section 8: Dependency Injection & Testable Architecture

Description: Master Dependency Injection in Python with FastAPI Depends(): inject database sessions, repositories, and services for extreme unit testability.
Level: Middle
URL: http://127.0.0.1:5000/python/middle/dependency_injection
"""

# --- Code Snippet 1 ---
# ❌ Creates real DB connection inside handler
@router.post("/users")
def create_user(data: UserCreate):
    db = SessionLocal() # Hardcoded dependency!
    repo = SqlAlchemyUserRepository(db)
    service = UserService(repo)
    return service.create_user(data)

# --- Code Snippet 2 ---
# ✅ Injected automatically via Depends() provider
@router.post("/users")
def create_user(
    data: UserCreate,
    service: UserService = Depends(get_user_service)
):
    return service.create_user(data)

# --- Code Snippet 3 ---
# ─── 1. DEPENDENCY PROVIDER FACTORY (api/dependencies.py) ─────────────────
def get_user_service(repo: UserRepository = Depends(get_user_repository)) -> UserService:
    return UserService(repository=repo)

# ─── 2. FASTAPI ROUTE CONSUMPTION (api/routes.py) ──────────────────────────
@router.post("/users", status_code=201)
def create_user(data: UserCreate, service: UserService = Depends(get_user_service)):
    return service.create_user(data)

# ─── 3. PYTEST OVERRIDE IN MOCK TEST (tests/test_users.py) ─────────────────
def get_mock_user_service() -> UserService:
    mock_repo = InMemoryUserRepository()
    return UserService(repository=mock_repo)

# Override real database service with mock during test execution
app.dependency_overrides[get_user_service] = get_mock_user_service

def test_create_user_fast_mock():
    client = TestClient(app)
    res = client.post("/users", json={"email": "test@test.com", "password": "pass"})
    assert res.status_code == 201

