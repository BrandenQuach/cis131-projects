# Lab: Books Database
# Author: Branden Quach
# November 24, 2024

# Libraries
import sqlite3
import pandas as pd

# Connection object
connection = sqlite3.connect('books.db')

# Selects all books for Author with the last name Quirk
pd.read_sql("""SELECT titles.title, titles.copyright, titles.ISBN
                FROM titles
                INNER JOIN author_ISBN
                    ON titles.ISBN = author_ISBN.ISBN
                INNER JOIN authors ON authors.ID = authors.ID
                WHERE authors.last = 'Quirk'
                ORDER BY title""", connection).head()
