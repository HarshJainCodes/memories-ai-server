from fastapi import APIRouter

from src.routes.chat import chat
from src.routes.upload import upload

router = APIRouter()

router.include_router(chat.router)
router.include_router(upload.router)
