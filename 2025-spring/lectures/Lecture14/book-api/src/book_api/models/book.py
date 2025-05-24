from datetime import datetime
from enum import StrEnum

from sqlmodel import Field, SQLModel


class Genre(StrEnum):
    FICTION = "fiction"
    NON_FICTION = "non_fiction"
    MYSTERY = "mystery"
    ROMANCE = "romance"
    SCIENCE_FICTION = "science_fiction"
    FANTASY = "fantasy"


class BookBase(SQLModel):
    title: str = Field(min_length=1, max_length=200)
    author: str = Field(min_length=1, max_length=100)
    isbn: str | None = Field(default=None, max_length=20)
    genre: Genre
    publication_year: int | None = Field(default=None, ge=1000)
    pages: int | None = Field(default=None, gt=0)
    description: str | None = None


class Book(BookBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime | None = None


class BookCreate(BookBase):
    pass


class BookGet(BookBase):
    id: int
    created_at: datetime
    updated_at: datetime | None = None


class BookUpdate(SQLModel):
    title: str | None = Field(default=None, min_length=1, max_length=200)
    author: str | None = Field(default=None, min_length=1, max_length=100)
    isbn: str | None = Field(default=None, max_length=20)
    genre: Genre | None = None
    publication_year: int | None = Field(default=None, ge=1000)
    pages: int | None = Field(default=None, gt=0)
    description: str | None = None
