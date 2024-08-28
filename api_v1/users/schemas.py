from pydantic import BaseModel,ConfigDict
from api_v1.books.schemas import BookRent

class UserBase(BaseModel):
    user_name: str
    books: list[BookRent] = []


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: int