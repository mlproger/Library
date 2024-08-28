from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import JSON


class User(Base):
    __tablename__ = "users"
    user_name: Mapped[str]
    books: Mapped[list[int]] = mapped_column(JSON)
