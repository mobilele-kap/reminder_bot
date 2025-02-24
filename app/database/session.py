from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from config import database

async_engine = create_async_engine(url=database.dsn_asyncpg)
sessions_db = async_sessionmaker(async_engine)
