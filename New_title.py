# Lab: Software Engineering with Abstract Classes and Abstract Methods
# Author: Branden Quach
# November 24, 2024

# Libraries
import sqlite3
import pandas as pd

# Connection object
connection = sqlite3.connect('books.db')

# SQLite3 cursor object
cursor = connection.cursor()

# Inserts new author
cursor = cursor.execute("""INSERT INTO authors (first, last)
                        Values('Branden', 'Quach')""")

# Inserts new ISBN to author's ID
cursor = cursor.execute("""INSERT INTO author_ISBN (ID, ISBN)
                        Values(6, '0123456789')""")

# Inserts new title, edition, and copyright to ISBN
cursor = cursor.execute("""INSERT INTO titles (ISBN, title, edition, copyright)
                        VALUES ('0123456789', 'Testing', 1, 2024)""")

# Views all titles
pd.read_sql('SELECT id, isbn, title, first, last FROM authors, titles',
             connection, index_col=['isbn'])
