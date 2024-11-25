# Lab: Books Database
# Author: Branden Quach
# November 24, 2024

# Libraries
import sqlite3
import pandas as pd

# Connection object
connection = sqlite3.connect('books.db')

# Views all authors' last names in descending order
pd.read_sql("SELECT last FROM authors ORDER BY last DESC", connection)
