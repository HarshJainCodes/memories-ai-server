import logging
from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.db import get_db

router = APIRouter()

logger = logging.getLogger("uvicorn.error")


@router.get("/chat")
async def chat_endpoint(db: Annotated[AsyncSession, Depends(get_db)]):

	await db.commit()

	return "This is the chat router v2"
