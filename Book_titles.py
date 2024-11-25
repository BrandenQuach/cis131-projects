import sqlite3
import pandas as pd

connection = sqlite3.connect('books.db')

pd.read_sql("SELECT title FROM titles ORDER BY title ASC", connection)
