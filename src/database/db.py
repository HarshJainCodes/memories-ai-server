import logging
import pyodbc
import os

from sqlalchemy import create_engine, text
from urllib.parse import quote_plus

from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger("sqlalchemy.engine")

logger.setLevel(logging.INFO)
logger.info(f"ODBC DRIVERS: {pyodbc.drivers()}")


connection_string = (
	"DRIVER={ODBC Driver 18 for SQL Server};"
	f"SERVER={os.getenv('SQL_SERVER')};"
	f"DATABASE={os.getenv('SQL_DATABASE')};"
	f"UID={os.getenv('SQL_USER_ID')};"
	f"PWD={os.getenv('SQL_PASSWORD')};"
	"Encrypt=yes;"
	"TrustServerCertificate=no;"
)

engine = create_engine(f"mssql+pyodbc:///?odbc_connect={quote_plus(connection_string)}")


def get_db():
	with engine.connect() as connection:
		result = connection.execute(
			text("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES")
		)
		print(result.fetchone())
	logger.info("this is the database")
