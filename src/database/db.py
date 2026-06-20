import os
from collections.abc import AsyncGenerator
from urllib.parse import quote_plus

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

connection_string = (
	"DRIVER={ODBC Driver 18 for SQL Server};"
	f"SERVER={os.getenv('SQL_SERVER')};"
	f"DATABASE={os.getenv('SQL_DATABASE')};"
	f"UID={os.getenv('SQL_USER_ID')};"
	f"PWD={os.getenv('SQL_PASSWORD')};"
	"Encrypt=yes;"
	"TrustServerCertificate=no;"
)

engine = create_async_engine(
	f"mssql+aioodbc:///?odbc_connect={quote_plus(connection_string)}"
)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
	async with async_session() as session:
		yield session
