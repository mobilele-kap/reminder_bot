from app.database import async_engine, sessions_db, UserOrm
from sqlalchemy import inspect
import app.database.models.user as user
from app.database.base import Base
from app.database.models.user import UserOrm
from sqlalchemy.schema import CreateTable


async def initialization():
    """Проверка создана ли таблица если нет, то создать"""
    async with async_engine.begin() as session:
        current_tables = await session.run_sync(
            lambda sync_conn: inspect(sync_conn).get_table_names()
        )
        await session.run_sync(Base.metadata.drop_all)
        await session.run_sync(Base.metadata.create_all)
    async with sessions_db() as session_db:
        user1 = user.UserOrm(telegram_id=11111, telegram_login='@test', deleted=True)
        session_db.add_all([user1])
        await session_db.commit()

        print(f'{current_tables=}')

