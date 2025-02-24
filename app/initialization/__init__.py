from .database import initialization as initialization_db


async def initialization():
    await initialization_db()


__all__ = (
    'initialization'
)