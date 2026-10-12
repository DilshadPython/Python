"""
Track 14: Production Engineering, Linux & Observability

Description: Master Senior Python Track 14: Production Engineering, Linux & Observability. Linux POSIX diagnostics, hardened multi-stage Dockerfiles, structured JSON logging, and correlation ID propagation.
Level: Senior
URL: http://127.0.0.1:5000/python/senior/production_engineering_observability
"""

# --- Code Snippet 1 ---
# Stage 1: Build
FROM python:3.12-slim-bookworm AS builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-install-project --no-dev

# Stage 2: Runtime
FROM python:3.12-slim-bookworm AS runtime
WORKDIR /app
RUN groupadd -r appuser && useradd -r -g appuser -d /app appuser
COPY --from=builder /app/.venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"
COPY --chown=appuser:appuser src/ /app/src/
USER appuser
EXPOSE 8000
# Exec form ensures process runs as PID 1 to receive SIGTERM cleanly
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]

