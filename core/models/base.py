from typing import Any

from sqlalchemy import JSON
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    __abstract__ = True
    type_annotation_map = {
        dict[str, Any]: JSON
    }
    id: Mapped[int] = mapped_column(primary_key=True)
