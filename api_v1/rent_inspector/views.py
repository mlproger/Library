from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.rent_inspector import actions
from core.models import db_helper

router = APIRouter(tags=["Rent"])

@router.patch("/{user_name}/{book_id}/{rent_date}")
async def set_rent(user_name: str, book_id: int, rent_date: str, session: AsyncSession = Depends(db_helper.session_dependency)):
    await actions.set_rent(
        user_name=user_name,
        book_id=book_id,
        rent_date=rent_date,
        session=session
    )