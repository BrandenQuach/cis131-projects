import sqlite3
import pandas as pd

connection = sqlite3.connect('books.db')

cursor = cursor.execute("""INSERT INTO authors (first, last)
            		Values('Branden', 'Quach')""")

cursor = cursor.execute("""INSERT INTO titles (ISBN, title, edition, copyright)
                        VALUES ('0123456789', 'Testing', 1, 2024)""")

pd.read_sql('SELECT id, isbn, title, first, last FROM authors, titles',
             connection, index_col=['isbn'])
