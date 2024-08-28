from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from .schemas import User
from . import crud
from core.models import db_helper
from .schemas import UserBase

router = APIRouter(tags=["User"])


"""
CREATE
"""

@router.post("/", response_model=User)
async def create_user(user: UserBase, session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.user_create(session=session, user=user)



"""
READ
"""
@router.get("/{user_name}/", response_model=User)
async def read_user(user_name: str, session: AsyncSession = Depends(db_helper.session_dependency)):
    user = await crud.user_read(user_name=user_name, session=session)
    if user:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User {user_name} not found"
    )