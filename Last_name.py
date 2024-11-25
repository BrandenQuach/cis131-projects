import sqlite3
import pandas as pd

connection = sqlite3.connect('books.db')

pd.read_sql("SELECT last FROM authors ORDER BY last DESC", connection)
