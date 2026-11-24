"""
Section 12: Production FastAPI Application Architecture

Description: Master production FastAPI application architecture: APIRouter modular endpoints, versioned API routing, Pydantic schemas, and application factory patterns.
Level: Middle
URL: http://127.0.0.1:5000/python/middle/fastapi_architecture
"""

# --- Code Snippet 1 ---
# ❌ 500 lines of DB, Models, and Routes in main.py
app = FastAPI()

class UserDB(Base): ...
class UserCreate(BaseModel): ...

@app.post("/users")
def create_user(): ...

# --- Code Snippet 2 ---
# ✅ Modular route in app/api/routes/users.py
router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse)
def create_user(data: UserCreate, srv = Depends()):
    return srv.create_user(data)

# --- Code Snippet 3 ---
# ─── 1. MASTER V1 ROUTER AGGREGATOR (app/api/api_v1.py) ───────────────────
from fastapi import APIRouter
from api.routes import auth, users, products

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(auth.router)
api_router.include_router(users.router)
api_router.include_router(products.router)

# ─── 2. APPLICATION FACTORY (app/main.py) ─────────────────────────────────
from fastapi import FastAPI
from api.api_v1 import api_router

def create_application() -> FastAPI:
    app = FastAPI(title="TeachCloud Enterprise API", version="1.0.0")
    app.include_router(api_router)
    return app

app = create_application()

