from functools import wraps
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
import dotenv

DB_CONFIG = dotenv.dotenv_values('.env')

SQLALCHEMY_DATABASE_URL = 'sqlite+aiosqlite:///./channel.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
metadata = MetaData()


if SQLALCHEMY_DATABASE_URL.startswith("sqlite"):
    engine = create_async_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )

elif SQLALCHEMY_DATABASE_URL.startswith("postgresql"):
    engine = create_async_engine(SQLALCHEMY_DATABASE_URL)
else:
    raise Exception("unknown database")

Base = declarative_base()

async_session = AsyncSession(bind=engine, expire_on_commit=False)


class Transactional:
    def __call__(self, func):
        @wraps(func)
        async def _transactional(*args, **kwargs):
            async with async_session as session:
                if kwargs.get("session"):
                    result = await func(*args, **kwargs)
                    await session.commit()
                    return result
                try:
                    kwargs["session"] = session
                    result = await func(*args, **kwargs)
                    await session.commit()
                except Exception as e:
                    # logger.exception(f"{type(e).__name__} : {str(e)}")
                    await session.rollback()
                    raise e

                return result

        return _transactional