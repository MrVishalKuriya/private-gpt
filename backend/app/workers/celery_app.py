from app.core.config import settings
from celery import Celery

celery_app = Celery(
    "worker",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL,
    include=["app.workers.tasks"],
)

celery_app.conf.task_routes = {"app.workers.tasks.*": "main-queue"}
