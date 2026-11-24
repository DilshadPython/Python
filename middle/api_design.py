"""
Section 14: RESTful API Design & OpenAPI Specifications

Description: Master production RESTful API design: HTTP verbs, status codes, pagination, filtering, rate limiting, JWT auth, idempotency, and OpenAPI schemas.
Level: Middle
URL: http://127.0.0.1:5000/python/middle/api_design
"""

# --- Code Snippet 1 ---
# ❌ Arbitrary verbs & status 200 for errors
POST /api/getUserById?id=123
POST /api/deleteUser?id=123
# Returns HTTP 200 OK: {"error": "Not Found"}

# --- Code Snippet 2 ---
from fastapi import APIRouter, Query, Depends
from schemas.user import UserResponse
from schemas.pagination import PageResponse

router = APIRouter(prefix="/api/v1/users", tags=["Users"])

@router.get("", response_model=PageResponse[UserResponse])
def list_users(
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    status: str | None = None,
    sort_by: str = Query("-created_at"),
    service = Depends()
) -> PageResponse[UserResponse]:
    return service.get_paginated_users(page, limit, status, sort_by)

