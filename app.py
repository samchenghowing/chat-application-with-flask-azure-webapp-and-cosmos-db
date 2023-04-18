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

def checkpassword(name, password):
    conn = get_db_connection()
    sql_select_query = """select * from users where name = ?"""
    user = conn.execute(sql_select_query, (name,)).fetchone()
    conn.close()

    if user is None:
        json_data = {"isvalid":False,"from client": request.remote_addr,
                        "attempt count": IPDict[request.remote_addr][0],
                        "status": "User not exist in database!"}
        return json_data

    hashedpw = user.get('pwHash')
    if check_password_hash(hashedpw, password):
        # update the format of hash before send to client
        user["pwHash"] = password
        IPDict[request.remote_addr].append(user.get('id'))
        json_data = {"isvalid":True, "from client": request.remote_addr,
                    "attempt count": IPDict[request.remote_addr][0], "User info": user}
        return json_data
    else:
        json_data = {"isvalid":False, "from client": request.remote_addr,
                    "attempt count": IPDict[request.remote_addr][0], "status": "password not match"}
        return json_data

# This route is for testing use only.
@app.route("/")
def main():
    return "Wellcome to COMP3334 Backend!" 

# This route is for testing use only.
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
    password = json_data['pwHash']

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
    conn.close()

    json_data = {"signup":True}
    return jsonify(json_data), 200

@app.route('/api/login', methods=['POST'])
@cross_origin()
def login():

    # check if brute force trying password to login
    if request.remote_addr not in IPDict:
        IPDict[request.remote_addr] = [0, datetime.now()]
    else:
        # reset the count to unblock user after 5 minutes
        if datetime.now() - IPDict[request.remote_addr][1] > timedelta(minutes=5):
            IPDict[request.remote_addr] = [0, datetime.now()]

        if IPDict[request.remote_addr][0] == 5:
            json_data = {"isvalid":False, "from client": request.remote_addr, 
                          "attempt count": IPDict[request.remote_addr][0], 
                          "status": "This IP is blocked 5 minutes since too many\
                                    failed login attempts"}
            return jsonify(json_data), 200
        IPDict[request.remote_addr][0] = IPDict[request.remote_addr][0] + 1

    json_data = request.get_json()
    name = json_data['name']
    password = json_data['pwHash']

    json_data = checkpassword(name, password)
    return jsonify(json_data), 200

@app.route('/api/chat/getupdate', methods=['POST'])
@cross_origin()
def getupdate():
    json_data = request.get_json()
    postId = json_data['postId']
    name = json_data['name']
    password = json_data['pwHash']

    isVaildRequest = checkpassword(name, password)
    if isVaildRequest['isvalid'] == False:
        return isVaildRequest, 200

    conn = get_db_connection()
    sql_select_query = """select * from chat where postId = ?"""
    chats = conn.execute(sql_select_query, (postId,)).fetchall()
    conn.close()

    return chats, 200

@app.route('/api/chat/send', methods=['POST'])
@cross_origin()
def chat():
    json_data = request.get_json()
    postId = json_data['postId']
    userID = json_data['userID']
    name = json_data['name']
    content = json_data['content']
    password = json_data['pwHash']

    isVaildRequest = checkpassword(name, password)
    if isVaildRequest['isvalid'] == False:
        return isVaildRequest, 200

    conn = get_db_connection()
    conn.execute("INSERT INTO chat (postId, userId, name, content) VALUES (?,?,?,?)",
                (postId, userID, name, content)
                )
    conn.commit()
    conn.close()
    
    json_data = {"send":True}
    return jsonify(json_data), 200


@app.route('/api/account/updateProfile', methods=['POST'])
@cross_origin()
def changePassword():
    json_data = request.get_json()
    userID = json_data['userID']
    name = json_data['name']
    oldpassword = json_data['oldpwHash']

    newname = json_data['newname']
    newemail = json_data['newemail']
    newpassword = json_data['newpwHash']
    isVaildRequest = checkpassword(name, oldpassword)
    if isVaildRequest['isvalid'] == False:
        return isVaildRequest, 200

    hash = generate_password_hash(newpassword)
    conn = get_db_connection()
    conn.execute("UPDATE users SET name=?, email=?, pwHash=? WHERE id=?",
                (newname, newemail, hash, userID)
                )
    conn.commit()
    sql_select_query = """select * from users where name = ?"""
    user = conn.execute(sql_select_query, (name,)).fetchone()
    conn.close()
    
    user["pwHash"] = newpassword
    json_data = {"isvalid":True, "from client": request.remote_addr,
                "attempt count": IPDict[request.remote_addr][0], "User info": user}
    return jsonify(json_data), 200

if __name__ == "__main__":
    app.run()
