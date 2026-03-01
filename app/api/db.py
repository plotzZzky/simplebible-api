import sqlite3
from pathlib import Path


verse_columns = 'id, book_id, chapter, verse, text'  # colunas da tabela de versiculos
book_columns = 'id, book_reference_id, testament_reference_id, name'  # colunas da tabela de livros


def find_in_bible(book=None, capt=None, vers=None):
    folder_path = Path(__file__).parent.resolve()
    db = f"{folder_path}/bible.sqlite"
    connection = sqlite3.connect(db)
    cursor = connection.cursor()

    query = check_params(book, capt, vers)
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result


def check_params(book=None, capt=None, vers=None):
    if vers:
        query = return_vers(book, capt, vers)
    elif capt:
        query = return_cap(book, capt)
    elif book:
        query = return_book(book)
    else:
        query = return_all_bible()

    return query


def return_all_bible():
    query = f"""
        SELECT *
        FROM verse
        JOIN book ON verse.book_id = book.id
    """

    return query


def return_book(book):
    query = f"""
        SELECT *
        FROM verse
        JOIN book ON verse.book_id = book.id
        WHERE book.name = '{book}'
    """

    return query


def return_cap(book, capt):
    query = f"""
        SELECT *
        FROM verse
        JOIN book ON verse.book_id = book.id
        WHERE book.name = '{book}' AND verse.chapter = '{capt}'
    """
    return query


def return_vers(book, capt, vers):
    query = f"""
        SELECT *
        FROM verse
        JOIN book ON verse.book_id = book.id
        WHERE book.name = '{book}' AND verse.chapter = '{capt}' AND verse.verse = '{vers}'
    """
    return query
