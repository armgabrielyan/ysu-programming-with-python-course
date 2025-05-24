from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlmodel import Session

from ..database.connection import get_session
from ..models.book import BookCreate, BookGet, BookUpdate, Genre
from ..services import book_service

router = APIRouter(
    prefix="/books",
    tags=["books"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)


@router.post("/", response_model=BookGet, status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate, session: Session = Depends(get_session)):
    return book_service.create_book(session, book)


@router.get("/", response_model=list[BookGet])
def read_books(
    skip: int = Query(0, ge=0, description="Number of books to skip"),
    limit: int = Query(10, ge=1, le=100, description="Number of books to return"),
    genre: Genre | None = Query(None, description="Filter by genre"),
    author: str | None = Query(None, description="Filter by author name"),
    session: Session = Depends(get_session),
):
    return book_service.get_books(
        session, skip=skip, limit=limit, genre=genre, author=author
    )


@router.get("/search", response_model=list[BookGet])
def search_books(
    query: str = Query(..., min_length=1, description="Search query"),
    session: Session = Depends(get_session),
):
    return book_service.search_books(session, query)


@router.get("/{book_id}", response_model=BookGet)
def get_book(book_id: int, session: Session = Depends(get_session)):
    book = book_service.get_book(session, book_id)
    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )
    return book


@router.put("/{book_id}", response_model=BookGet)
def update_book(
    book_id: int, book_update: BookUpdate, session: Session = Depends(get_session)
):
    book = book_service.update_book(session, book_id, book_update)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )
    return book


@router.delete("/{book_id}")
def delete_book(book_id: int, session: Session = Depends(get_session)):
    success = book_service.delete_book(session, book_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )
    return {"message": "Book deleted successfully"}
