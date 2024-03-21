"""
This program builds the author_book_publisher Sqlite database from the
author_book_publisher.csv file.
"""

import os
import csv
import pathlib
from importlib import resources
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from project.models.book import Book, Base
import project

#from project.models import Base
#from project.models import Book

def get_author_book_publisher_data(filepath):
    """
    This function gets the data from the csv file
    """
    with open(filepath) as csvfile:
        csv_reader = csv.DictReader(csvfile)
        data = [row for row in csv_reader]
        return data

def populate_database(session, author_book_publisher_data):
    # insert the data
    for row in author_book_publisher_data:
        book = (
            session.query(Book)
            .filter(Book.title == row['title'])
            .one_or_none()
        )
        if book is None:
            book = Book(
                first_name=row['first_name'],
                last_name=row['last_name'],
                title=row['title'],
                publisher=row['publisher'],
            )
            session.add(book)
        session.commit()

    session.close()

def main():
    print('starting')
    # csvfile = './project/data/author_book_publisher.csv'
    # data = get_author_book_publisher_data(csvfile)
    # author_book_publisher_data = data
    print("paths:", pathlib.Path(project.__file__), pathlib.Path(project.__file__).parent)

    data = get_author_book_publisher_data(pathlib.Path(project.__file__).parent / 'data/author_book_publisher.csv')
    author_book_publisher_data = data

    print("data table:", author_book_publisher_data)

    sqlite_filepath = pathlib.Path(project.__file__).parent / 'data/author_book_publisher.db'
    print("database file:", sqlite_filepath)

    # does the database exist?
    if os.path.exists(sqlite_filepath):
        os.remove(sqlite_filepath)

    # create the database
    # engine = create_engine(f"sqlite:///{sqlite_filepath}")
    engine = create_engine("mysql+mysqldb://nathan2:Coal@localhost/data5zero")

    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    populate_database(session, author_book_publisher_data)


if __name__ == "__main__":
    main()
