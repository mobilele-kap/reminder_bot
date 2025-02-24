from app.database import async_engine, sessions_db, UserOrm
from sqlalchemy import inspect


async def initialization():
    """Проверка создана ли таблица если нет, то создать"""
    async with async_engine.begin() as session:
        tables = await session.run_sync(
            lambda sync_conn: inspect(sync_conn).get_table_names()
        )
        print(f'{tables=}')