from pydantic import BaseModel, ConfigDict
from typing import ClassVar, Optional


#Каркасс
class BookBase(BaseModel):
    name: str
    author: str
    isRent: bool = False
    rentDate: Optional[str]


class BookRent(BookBase):
    rentDate: str



#Возврат
class Book(BookBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
