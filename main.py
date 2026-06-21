import logging
import os

import uvicorn
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("uvicorn.error")


if __name__ == "__main__":
	if os.getenv("ENV") == "DEVELOPMENT":
		logger.info("Running in Development Mode")
		uvicorn.run(
			"src.main:app",
			host="0.0.0.0",
			port=8000,
			reload=True,
			ssl_certfile="localhost.pem",
			ssl_keyfile="localhost-key.pem",
		)
	else:
		logger.info("Running in Production Mode")
		uvicorn.run("src.main:app", host="0.0.0.0", port=8000)
