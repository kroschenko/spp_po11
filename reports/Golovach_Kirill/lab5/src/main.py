from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, init_db
from crud import (
    create_book, get_books, get_book, update_book, delete_book
)

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Эндпоинты для Book
@app.post("/books/")
def create_book_endpoint(book: dict, db: Session = Depends(get_db)):
    return create_book(db, book)

@app.get("/books/")
def get_books_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_books(db, skip=skip, limit=limit)

@app.get("/books/{book_id}")
def get_book_endpoint(book_id: int, db: Session = Depends(get_db)):
    book = get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.put("/books/{book_id}")
def update_book_endpoint(book_id: int, book: dict, db: Session = Depends(get_db)):
    updated_book = update_book(db, book_id, book)
    if not updated_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_book

@app.delete("/books/{book_id}")
def delete_book_endpoint(book_id: int, db: Session = Depends(get_db)):
    book = delete_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted"}
