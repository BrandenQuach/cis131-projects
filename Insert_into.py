# Lab: Books Database
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

# Views all authors
pd.read_sql('SELECT id, first, last FROM authors',
             connection, index_col=['id'])
