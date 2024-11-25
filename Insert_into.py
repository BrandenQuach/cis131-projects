import sqlite3

connection = sqlite3.connect('books.db')

cursor = connection.cursor()

cursor = cursor.execute("""INSERT INTO authors (first, last)
                        Values('Jeff', 'Johnson')""")
