import logging
from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.db import get_db
from src.database.db_models import memories_db_models

router = APIRouter()

logger = logging.getLogger("uvicorn.error")


@router.get("/chat")
async def chat_endpoint(db: Annotated[AsyncSession, Depends(get_db)]):

	result = await db.execute(
		select(memories_db_models.ChatbotConversations.conversation_id).where(
			memories_db_models.ChatbotConversations.user_email
			== "harshjain17may@gmail.com"
		)
	)

	all_users = result.fetchall()

	logger.info(all_users)
	return "This is the chat router v2"
