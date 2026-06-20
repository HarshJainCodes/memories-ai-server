import logging

from fastapi import FastAPI

from src.routes import routes

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("uvicorn.error")

app = FastAPI()

logger.info("running the fastapi server")
app.include_router(routes.router)
