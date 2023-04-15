from datetime import datetime, timedelta
import sqlite3
from flask import Flask,request,jsonify
from flask_cors import CORS, cross_origin
from werkzeug.security import generate_password_hash, check_password_hash

# Client IPDict
IPDict = {}

# https://testdriven.io/blog/csrf-flask/
app = Flask(__name__)
cors = CORS(app)
app.config.update(
    DEBUG=True,
    CORS_HEADERS='Content-Type',
)

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = dict_factory
    return conn

@app.route("/")
def main():
    return "Wellcome to COMP3334 Backend!" 

@app.route('/api/users')
@cross_origin()
def get_users():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()

    return users, 200

@app.route('/api/signup', methods=['POST'])
@cross_origin()
def signup():
    json_data = request.get_json()

    name = json_data['name']
    password = json_data['password']

    # TO-DO: avoid sql injection

    # check if user exist in database
    conn = get_db_connection()
    sql_select_query = """select * from users where name = ?"""
    res = conn.execute(sql_select_query, (name,)).fetchone()
    if res is not None:
        json_data = {"signup":False, "status": "User alreafy exist in database!"}
        return jsonify(json_data), 200

    # TO-DO: email verify

    hash = generate_password_hash(password)
    conn.execute("INSERT INTO users (name, pwHash, confirmed) VALUES (?, ?, ?)",
                (name, hash, 0)
                )
    

    conn.commit()
    # users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()

    json_data = {"signup":True}
    return jsonify(json_data), 200


@app.route('/api/login', methods=['POST'])
@cross_origin()
def login():
    json_data = request.get_json()

    # check if brute force trying password to login
    if request.remote_addr not in IPDict:
        IPDict[request.remote_addr] = [0, datetime.now()]
    else:
        # reset the count to unblock user after a minute
        if datetime.now() - IPDict[request.remote_addr][1] > timedelta(minutes=1):
            IPDict[request.remote_addr] = [0, datetime.now()]

        if IPDict[request.remote_addr][0] == 5:
            json_data = {"isvalid":False, "from client": request.remote_addr, 
                          "attempt count": IPDict[request.remote_addr][0], 
                          "status": "This IP is blocked 1 minutes since too many\
                                    failed login attempts"}
            return jsonify(json_data), 200
        IPDict[request.remote_addr][0] = IPDict[request.remote_addr][0] + 1

    name = json_data['name']
    password = json_data['password']


    # TO-DO: avoid sql injection

    conn = get_db_connection()
    sql_select_query = """select * from users where name = ?"""
    user = conn.execute(sql_select_query, (name,)).fetchone()
    conn.close()

    if user is None:
        json_data = {"isvalid":False,"from client": request.remote_addr,
                        "attempt count": IPDict[request.remote_addr],
                        "status": "User not exist in database!"}
        return jsonify(json_data), 200

    hashedpw = user.get('pwHash')
    if check_password_hash(hashedpw, password):
        user.pop("pwHash")
        json_data = {"isvalid":True, "from client": request.remote_addr,
                    "attempt count": IPDict[request.remote_addr], "User info": user}
        return jsonify(json_data), 200
    else:
        json_data = {"isvalid":False, "from client": request.remote_addr,
                    "attempt count": IPDict[request.remote_addr], "status": "password not match"}
        return jsonify(json_data), 200


@app.route('/api/confirm/<token>')
@cross_origin()
def confirm_email():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    
    return users, 200

if __name__ == "__main__":
    app.run()
