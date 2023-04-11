# This file will create init and dummy data to database

import sqlite3
import hashlib

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content for the first post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'Content for the second post')
            )
inStr = "Alice'spassword"
hash = hashlib.sha256(inStr.encode('utf-8')).hexdigest()

cur.execute("INSERT INTO users (name, pwHash) VALUES (?, ?)",
            ('Alice', hash)
            )

connection.commit()
connection.close()