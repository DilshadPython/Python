"""
Section 15: Authentication & Security Architecture

Description: Master production Python backend security: Argon2id/bcrypt password hashing, JWT access & refresh tokens, OAuth2, RBAC, SQLi/XSS/CSRF mitigations, CORS, and secrets management.
Level: Middle
URL: http://127.0.0.1:5000/python/middle/auth_security
"""

# --- Code Snippet 1 ---
# ❌ Plaintext password & hardcoded JWT secret!
user.password = "mypassword123"
SECRET_KEY = "12345"

# Vulnerable SQL Injection query
db.execute(f"SELECT * FROM users WHERE id='{user_id}'")

# --- Code Snippet 2 ---
# ✅ Salted Argon2id hashing & env settings
user.hashed_pwd = pwd_context.hash(plain_pwd)
SECRET_KEY = settings.SECRET_KEY

# Parameterized ORM query blocks SQLi
select(UserModel).where(UserModel.id == user_id)

# --- Code Snippet 3 ---
from passlib.context import CryptContext
from jose import jwt
from fastapi import Depends, HTTPException, status

pwd_context = CryptContext(schemes=["argon2", "bcrypt"], deprecated="auto")

def require_role(allowed_roles: list[str]):
    def role_checker(token: str = Depends(oauth2_scheme)):
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        if payload.get("role") not in allowed_roles:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
        return payload
    return role_checker

