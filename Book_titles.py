# Lab: Software Engineering with Abstract Classes and Abstract Methods
# Author: Branden Quach
# November 24, 2024

# Libraries
import sqlite3
import pandas as pd

# Connection object
connection = sqlite3.connect('books.db')

# View all titles in ascending order
pd.read_sql("SELECT title FROM titles ORDER BY title ASC", connection)
