from fastapi import APIRouter
from app.schemas.book_schema import BookCreate
from app.repository.book_repo import create_book, get_books

router = APIRouter(prefix="/books", tags=["Books"])


@router.post("/")
def add_book(book: BookCreate):
    return create_book(book)


@router.get("/")
def all_books():
    return get_books()
