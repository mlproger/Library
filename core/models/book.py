from typing import Optional

from .base import Base
from sqlalchemy.orm import Mapped, mapped_column


class Book(Base):
    __tablename__ = "books"
    name: Mapped[str]
    author: Mapped[str]
    isRent: Mapped[bool]
    rentDate: Mapped[Optional[str]]