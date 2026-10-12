"""
Section 18: Caching, Message Queues & Background Workers

Description: Master production Python background processing and caching: Redis Cache-Aside pattern, Celery distributed task queues, RabbitMQ brokers, and automatic task retries.
Level: Middle
URL: http://127.0.0.1:5000/python/middle/caching_background_workers
"""

# --- Code Snippet 1 ---
# ❌ Blocks HTTP response thread for 5+ seconds!
@router.post("/register")
def register_user(data: UserRegister):
    user = db.create(data)
    send_smtp_email_sync(user.email)  # Blocking I/O!
    return user

# --- Code Snippet 2 ---
# ✅ Enqueues task & returns HTTP 202 immediately
@router.post("/register", status_code=202)
def register_user(data: UserRegister):
    user = db.create(data)
    send_welcome_email_task.delay(user.email)
    return {"message": "User created, email queued"}

# --- Code Snippet 3 ---
from core.celery_app import celery_app

@celery_app.task(bind=True, max_retries=3)
def send_welcome_email_task(self, email: str):
    try:
        smtp_service.send_welcome(email)
    except Exception as exc:
        # Exponential backoff retry calculation: 60 * (2 ^ retries)
        countdown = 60 * (2 ** self.request.retries)
        raise self.retry(exc=exc, countdown=countdown)

