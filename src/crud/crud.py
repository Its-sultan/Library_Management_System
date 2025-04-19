
from sqlalchemy.orm import Session
from src.models import Book 
from src.schemas import BookCreate, BookUpdate


def get_books(db: Session):
    return db.query(Book).all()


def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id.first)


def create_book(db : Session, book: BookCreate):
    new_book = Book(title = book.title, author = book.author, published_year = book.published_year, isbn = book.isbn)

    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


def update_books(db: Session, book_id:int, book: BookUpdate):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book:
        for key, value in book.dict(exclude_unset = True).items():
            setattr(db_book, key, value)
        db.commit()
        db.refresh(db_book)
    return db_book


def delete_book(db: Session, book_id:int):
    db_book = db.query(Book).filter(Book.id == book_id).firts()
    if db_book:
        db.delete(db_book)
        db.commit()
    return db_book            