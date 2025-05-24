from datetime import datetime

from sqlmodel import Session, select

from ..models.book import Book, BookCreate, BookUpdate, Genre


def create_book(session: Session, book: BookCreate) -> Book:
    """Create a new book in the database."""

    db_book = Book.model_validate(book)
    session.add(db_book)
    session.commit()
    session.refresh(db_book)

    return db_book


def get_book(session: Session, book_id: int) -> Book | None:
    """Get a book by its ID from the database."""
    return session.get(Book, book_id)


def get_books(
    session: Session,
    skip: int = 0,
    limit: int = 100,
    genre: Genre | None = None,
    author: str | None = None,
) -> list[Book]:
    statement = select(Book)

    if genre is not None:
        statement = statement.where(Book.genre == genre)
    if author is not None:
        statement = statement.where(Book.author.contains(author)) # type: ignore

    statement = statement.offset(skip).limit(limit)

    books = session.exec(statement).all()

    return list(books)


def update_book(session: Session, book_id: int, book_update: BookUpdate) -> Book | None:
    """Update an existing book in the database."""
    
    book = session.get(Book, book_id)
    if book is None:
        return None

    book_data = book_update.model_dump(exclude_unset=True)
    book_data["updated_at"] = datetime.now()

    for key, value in book_data.items():
        setattr(book, key, value)

    session.add(book)
    session.commit()
    session.refresh(book)

    return book


def delete_book(session: Session, book_id: int) -> bool:
    """Delete a book from the database by its ID."""

    book = session.get(Book, book_id)
    if book is None:
        return False

    session.delete(book)
    session.commit()

    return True


def search_books(session: Session, query: str) -> list[Book]:
    """Search for books by title, author or description."""

    statement = select(Book).where(
        Book.title.contains(query) # type: ignore
        | Book.author.contains(query) # type: ignore
        | Book.description.contains(query) # type: ignore
    )

    books = session.exec(statement).all()

    return list(books)
