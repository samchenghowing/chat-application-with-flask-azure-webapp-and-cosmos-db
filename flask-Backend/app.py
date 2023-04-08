import os
import socket
from flask import Flask,request,jsonify
import sqlite3
import hashlib

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def calculation_hash(password, salt, pepper="G30", iteration=1):
    # Inputs
    # password is the user's password in plain text
    # salt is the unique salt per user and is randomly generated, store in database
    # pepper is the common pepper for all users and is randomly generated, store in application.
    # iteration is the number of iterations

    # Output:
    # The password hash
    # Hash = sha512(salt+password+pepper)
    # As long as iteration is greater than 0
    # hash = sha512(hash)
    # Decrement iteration
    inStr = password + salt + pepper

    while iteration > 0:
        hash = hashlib.sha256(inStr.encode('utf-8')).hexdigest()
        iteration = iteration - 1

    return hash

@app.route("/")
def main():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return str(posts) 

@app.route('/api/about')
def about():
    return 'I am '+socket.gethostname()

@app.route('/api/users')
def get_users():
    json_data = [{"name":"alice","age":18},{"name":"bob", "age": 22}]
    return jsonify(json_data),200

@app.route('/api/login', methods=('POST'))
def login():
    print(request)
    name = request.form['name']
    password = request.form['password']

    conn = get_db_connection()
    # conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
    #                 (title, content))

    conn.commit()
    conn.close()

    return jsonify(json_data), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True, use_reloader=False)   
