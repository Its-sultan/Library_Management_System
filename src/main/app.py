
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database import SessionLocal, engine, Base
from src.models import Book
from src.schemas import BookCreate, BookUpdate, BookResponse
from src.crud import get_books, get_book, create_book, update_books, delete_book
from src.main.routes import books

app = FastAPI(title="Library Management System API")

Base.metadata.create_all(bind = engine)

app.include_router(books)

def get_db():
    db = SessionLocal()
    try:
         yield db
    finally:
        db.close()
        
@app.get("/")
def home():
    return {"message": "Welcome to the Library Management System API"}     

@app.get("/books")
async def get_books(db: Session = Depends(get_db)):
    return db.query(Book).all()   
        
@app.post("/books/", response_model = BookResponse)
def create_new_book(book: BookCreate, db: Session = Depends(get_db)):
    return create_book(db, book)

@app.get("/books/", response_model = list[BookResponse])
def read_books(db: Session = Depends(get_db)):
    return get_books(db)

@app.get("/books/{book_id}", response_model = BookResponse)
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = get_book(db, book_id)
    if not book:
        raise HTTPException(status_code = 404, detail = "Book not found")
    return book               

@app.put("/books/{book_id}", response_model = BookResponse)
def update_book_details(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    updated_book = update_books(db, book_id, book)
    if not updated_book:
        raise HTTPException(status_code = 404, detail = "Book not found")
    return updated_book

@app.delete("/books/{book_id}")
def remove_book(book_id: int, db: Session = Depends(get_db)):
    deleted_book = delete_book(db, book_id)
    if not deleted_book:
        raise HTTPException(status_code = 404, detail= "Book not found")
    return {"message": "Book deleted successfully"}



        