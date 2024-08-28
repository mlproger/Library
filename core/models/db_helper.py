from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, async_scoped_session, AsyncSession
from core.config import config
from asyncio import current_task


class DatabaseHelper:
    def __init__(self):
        self.engine = create_async_engine(
            url=config.db_url,
            echo=config.db_echo
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            expire_on_commit=False,
            autocommit=False
        )

    def get_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task
        )
        return session


    async def session_dependency(self) -> AsyncSession:
        async with self.session_factory() as session:
            yield session
            await session.close()

db_helper = DatabaseHelper()
