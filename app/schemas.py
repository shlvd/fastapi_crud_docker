from datetime import datetime
from typing import List
from pydantic import BaseModel


class BookBaseSchema(BaseModel):
    """Base schema for a book."""
    id: str = None
    title: str
    content: str
    category: str = None
    published: bool = False
    createdAt: datetime = None
    updatedAt: datetime = None

    class Config:
        """Config for the book base schema."""
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class ListBookResponse(BaseModel):
    """Response schema for a list of books."""
    status: str
    results: int
    books: List[BookBaseSchema]
