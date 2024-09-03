from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Book
from api_v1.books.schemas import BookRent, BookBase
import api_v1.books.crud as book_crud
import api_v1.users.crud as user_crud

async def set_rent(user_name: str, book_id: int, rent_date: str, session: AsyncSession):
    book = await book_crud.get_book(session=session, book_id=book_id)
    setattr(book, "rentDate", rent_date)
    await session.commit()

    user = await user_crud.user_read(session=session, user_name=user_name)
    print(user)
    books = user.books
    if not books:
        books = []
    books.append(book_id)
    print(books)
    setattr(user, "books", books)
    await session.commit()

    if not book:
        HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Can't set rent. Book with {book_id} not found"
        )


async def delete_rent():
    pass