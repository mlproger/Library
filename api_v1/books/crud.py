from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Book
from sqlalchemy.engine import Result
from .schemas import BookBase, BookRent

"""
CREATE
"""

async def create_book(session: AsyncSession, book: BookBase) -> Book | None:
    print(Book(**book.model_dump()))
    book = Book(**book.model_dump())
    session.add(book)
    await session.commit()
    await session.refresh(book)
    return book


async def create_books(session: AsyncSession, books: list[BookBase]) -> list[Book] | None:
    result: list[Book] = []
    for book in books:
        book = Book(**book.model_dump())
        session.add(book)
        await session.commit()
        await session.refresh(book)
        result.append(book)
    return result





"""
READ 
"""
async def get_book(session: AsyncSession, book_id: int) -> Book | None:
    return await session.get(Book, book_id)

async def get_books(session: AsyncSession) -> list[Book] | None:
    stmt = select(Book).order_by(Book.id)
    result: Result = await session.execute(stmt)
    books = result.scalars().all()
    return list(books)


"""
UPDATE
"""

async def set_rent(session: AsyncSession, rent_date: str, book: Book) -> Book | None:
    setattr(book, "rentDate", rent_date)
    await session.commit()
    return book