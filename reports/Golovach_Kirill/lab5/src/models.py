from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

# Связь многие-ко-многим между Collection и Book
collection_book = Table(
    'collection_book', Base.metadata,
    Column('collection_id', Integer, ForeignKey('collections.id')),
    Column('book_id', Integer, ForeignKey('books.id'))
)

class Genre(Base):
    __tablename__ = "genres"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False, unique=True)
    books = relationship("Book", back_populates="genre")

class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    biography = Column(String(500))
    books = relationship("Book", back_populates="author")

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String(250))
    price = Column(Float, nullable=False)
    genre_id = Column(Integer, ForeignKey("genres.id"))
    author_id = Column(Integer, ForeignKey("authors.id"))
    genre = relationship("Genre", back_populates="books")
    author = relationship("Author", back_populates="books")
    collections = relationship("Collection", secondary=collection_book, back_populates="books")

class Collection(Base):
    __tablename__ = "collections"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(250))
    total_price = Column(Float)
    books = relationship("Book", secondary=collection_book, back_populates="collections")
