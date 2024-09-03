from sqlalchemy.engine import Result
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import UserBase
from core.models import User

"""
CREATE
"""


async def user_create(session: AsyncSession, user: UserBase) -> User | None:
    user = User(**user.model_dump())
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user


"""
READ
"""


async def user_read(session: AsyncSession, user_name: str) -> User | None:
    stmt = select(User).where(User.user_name == user_name)
    result: Result = await session.execute(stmt)
    user = result.scalars().all()
    if user:
        return list(user)[0]
    return None


async def users_read(session: AsyncSession) -> list[User] | None:
    stmt = select(User).order_by(User.id)
    result: Result = await session.execute(stmt)
    users = result.scalars().all()
    return list(users)
