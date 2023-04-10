from datetime import date, datetime, timedelta
import logging
import os
import socket
from flask import Flask,request,jsonify
import sqlite3
import hashlib

# Client IPDict
IPDict = {}

app = Flask(__name__)

def initLogger():
    """Create a logger and log file named with today's day + connectionLog.txt """
    today = date.today()
    if not os.path.exists("Logs"):
        os.makedirs("Logs")
    logging.basicConfig(filename=f'Logs/{today.strftime("%d%m%y") + "connectionLog.txt"}',
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG)
    logging.getLogger('server').info("The logger is initialized")

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

@app.route('/api/login', methods=['POST'])
def login():
    json_data = request.get_json()
    print(json_data)


    if request.remote_addr not in IPDict:
        IPDict[request.remote_addr] = [0, datetime.now()]
    else:
        # reset the count to unblock user after a minute
        if datetime.now() - IPDict[request.remote_addr][1] > timedelta(minutes=1):
            IPDict[request.remote_addr] = [0, datetime.now()]

        if IPDict[request.remote_addr][0] == 5:
            json_data = [{"login":False, "attempt count": IPDict[request.remote_addr][0], 
                          request.remote_addr: "This IP is blocked 1 minutes since too many\
                             failed login attempts"}]
            return jsonify(json_data), 200
        IPDict[request.remote_addr][0] = IPDict[request.remote_addr][0] + 1

    name = json_data['name']
    password = json_data['password']

    # TO-DO: avoid sql injection
    conn = get_db_connection()
    # conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
    #                 (title, content))

    conn.commit()
    conn.close()

    json_data = [{"login":True, "from client": request.remote_addr,
                  "attempt count": IPDict[request.remote_addr]}]
    return jsonify(json_data), 200

if __name__ == "__main__":
    # app.run(ssl_context='adhoc', host="0.0.0.0", port=8080, debug=True, use_reloader=False) 
    app.run()  # run this on Azure App Service
