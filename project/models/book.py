from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Book(Base):
    __tablename__ = "book"
    book_id = Column(Integer, primary_key=True)
    first_name = Column(String(64))
    last_name = Column(String(64))
    title = Column(String(255))
    publisher = Column(String(255))

