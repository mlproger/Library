from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .schemas import Book, BookBase
from core.models import db_helper

router = APIRouter(tags=["Books"])


"""
CREATE
"""

@router.post("/", response_model=Book)
async def add_book(book: BookBase, session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.create_book(session=session, book=book)

@router.post("/s/", response_model=list[Book])
async def add_books(books: list[BookBase], session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.create_books(session=session, books=books)



"""
READ
"""

@router.get("/{book_id}/", response_model=Book)
async def get_book(book_id: int, session: AsyncSession = Depends(db_helper.session_dependency)):
    book = await crud.get_book(session=session, book_id=book_id)
    if book:
        return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Book {book_id} not found"
    )


@router.get("/", response_model=list[Book])
async def get_books(session: AsyncSession = Depends(db_helper.session_dependency)):
    books = await crud.get_books(session=session)
    print(books)
    if books:
        return books
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Books not found"
    )


"""
UPDATE
"""

@router.patch("/sent_rent/{book_id}/{rent_date}", response_model=Book)
async def update_rent(book_id: int, rent_date: str, session: AsyncSession = Depends(db_helper.session_dependency)):
    book = await crud.get_book(session=session, book_id=book_id)
    await crud.set_rent(session,rent_date,book)
    return book
