from app.initialization import initialization


async def load():
    await initialization()


__all__ = (
    'load'
)
