import sqlite3
import pandas as pd

connection = sqlite3.connect('books.db')

pd.read_sql("""SELECT isbn, title, edition, copyright, last
            FROM authors, titles
            WHERE last LIKE '%Quirk'
            ORDER BY last ASC""", connection)
