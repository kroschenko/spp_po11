from sqlalchemy.orm import Session
from models import Book, Genre, Author, Collection

# CRUD для Book
def create_book(db: Session, book_data: dict):
    db_book = Book(**book_data)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Book).offset(skip).limit(limit).all()

def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def update_book(db: Session, book_id: int, book_data: dict):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book:
        for key, value in book_data.items():
            setattr(db_book, key, value)
        db.commit()
        db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book:
        db.delete(db_book)
        db.commit()
    return db_book

# CRUD для Genre
def create_genre(db: Session, genre_data: dict):
    db_genre = Genre(**genre_data)
    db.add(db_genre)
    db.commit()
    db.refresh(db_genre)
    return db_genre

def get_genres(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Genre).offset(skip).limit(limit).all()

def get_genre(db: Session, genre_id: int):
    return db.query(Genre).filter(Genre.id == genre_id).first()

def update_genre(db: Session, genre_id: int, genre_data: dict):
    db_genre = db.query(Genre).filter(Genre.id == genre_id).first()
    if db_genre:
        for key, value in genre_data.items():
            setattr(db_genre, key, value)
        db.commit()
        db.refresh(db_genre)
    return db_genre

def delete_genre(db: Session, genre_id: int):
    db_genre = db.query(Genre).filter(Genre.id == genre_id).first()
    if db_genre:
        db.delete(db_genre)
        db.commit()
    return db_genre

# CRUD для Author
def create_author(db: Session, author_data: dict):
    db_author = Author(**author_data)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def get_authors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Author).offset(skip).limit(limit).all()

def get_author(db: Session, author_id: int):
    return db.query(Author).filter(Author.id == author_id).first()

def update_author(db: Session, author_id: int, author_data: dict):
    db_author = db.query(Author).filter(Author.id == author_id).first()
    if db_author:
        for key, value in author_data.items():
            setattr(db_author, key, value)
        db.commit()
        db.refresh(db_author)
    return db_author

def delete_author(db: Session, author_id: int):
    db_author = db.query(Author).filter(Author.id == author_id).first()
    if db_author:
        db.delete(db_author)
        db.commit()
    return db_author

# CRUD для Collection
def create_collection(db: Session, collection_data: dict):
    db_collection = Collection(**collection_data)
    db.add(db_collection)
    db.commit()
    db.refresh(db_collection)
    return db_collection

def get_collections(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Collection).offset(skip).limit(limit).all()

def get_collection(db: Session, collection_id: int):
    return db.query(Collection).filter(Collection.id == collection_id).first()

def update_collection(db: Session, collection_id: int, collection_data: dict):
    db_collection = db.query(Collection).filter(Collection.id == collection_id).first()
    if db_collection:
        for key, value in collection_data.items():
            setattr(db_collection, key, value)
        db.commit()
        db.refresh(db_collection)
    return db_collection

def delete_collection(db: Session, collection_id: int):
    db_collection = db.query(Collection).filter(Collection.id == collection_id).first()
    if db_collection:
        db.delete(db_collection)
        db.commit()
    return db_collection

# Добавление и удаление книги в подборку
def add_book_to_collection(db: Session, collection_id: int, book_id: int):
    collection = db.query(Collection).filter(Collection.id == collection_id).first()
    book = db.query(Book).filter(Book.id == book_id).first()
    if collection and book:
        collection.books.append(book)
        db.commit()
        db.refresh(collection)
    return collection

def remove_book_from_collection(db: Session, collection_id: int, book_id: int):
    collection = db.query(Collection).filter(Collection.id == collection_id).first()
    book = db.query(Book).filter(Book.id == book_id).first()
    if collection and book:
        collection.books.remove(book)
        db.commit()
        db.refresh(collection)
    return collection
