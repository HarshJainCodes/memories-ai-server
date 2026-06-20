import logging
from fastapi import APIRouter


router = APIRouter()

logger = logging.getLogger("uvicorn.error")


@router.get("/chat")
def chat_endpoint():

	logger.error("request to chat endpoint appeared")

	from src.database.db import get_db

	get_db()
	return "This is the chat router v2"
