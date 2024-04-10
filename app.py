import json
from datetime import datetime, timedelta
from flask import Flask,request,jsonify, session
from flask_cors import CORS, cross_origin
from flask_socketio import emit, join_room, leave_room, SocketIO

from werkzeug.security import generate_password_hash, check_password_hash
from azure.cosmos import CosmosClient
from azure.identity import DefaultAzureCredential

endpoint = "https://comp3334nosqldb.documents.azure.com:443/"

DATABASE_NAME = "comp3334DB"
CONTAINER_NAME = "container1"

credential = DefaultAzureCredential()
client = CosmosClient(url=endpoint, credential=credential)

dataBase = client.get_database_client(DATABASE_NAME)
container = dataBase.get_container_client(CONTAINER_NAME)

# Client IPDict
IPDict = {}

app = Flask(__name__)
cors = CORS(app)
app.config.update(
    DEBUG=True,
    CORS_HEADERS='Content-Type',
)
socketio = SocketIO(app, cors_allowed_origins="*", engineio_logger=True)


@socketio.on('joined')
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    join_room(room)
    emit('status', {'msg': session.get('name') + ' has entered the room.'}, room=room)

def checkpassword(name, password):

    results = container.query_items(
        query="SELECT * FROM c WHERE c.name = @name", 
        parameters=[dict(name="@name", value=name)], 
        enable_cross_partition_query=True
    )
    items = [item for item in results]

    if len(items) == 0:
        json_data = {"isvalid":False,"from client": request.remote_addr,
                        "attempt count": IPDict[request.remote_addr][0],
                        "status": "User not exist in database!"}
        return json_data
    
    user = items[0]

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
    # https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/quickstart-python?tabs=azure-portal%2Cpasswordless%2Clinux%2Csign-in-azure-cli%2Csync#get-an-item
    existing_item = container.read_item(
        item="001",
        partition_key="001",
    )
    return jsonify(existing_item), 200

@app.route('/api/signup', methods=['POST'])
@cross_origin()
def signup():
    json_data = request.get_json()

    results = container.query_items(
        query="SELECT * FROM c WHERE c.name = @name", 
        parameters=[dict(name="@name", value=json_data['name'])], 
        enable_cross_partition_query=True
    )
    items = [item for item in results]

    if len(items) != 0:
        json_data = {
            "signup":False, 
            "status": "User alreafy exist in database!"
            }
        return jsonify(json_data), 200

    # TO-DO: email verify

    hash = generate_password_hash(json_data['pwHash'])
    parameters = {
        "id": json_data['name'], 
        "name": json_data['name'],
        "pwHash": hash,
        "confirmed": 0
    }
    userProxy = dataBase.create_user(parameters)
    
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
            json_data = {
                "isvalid":False, "from client": request.remote_addr, 
                "attempt count": IPDict[request.remote_addr][0], 
                "status": "This IP is blocked 5 minutes since too many\
                    failed login attempts"}
            return jsonify(json_data), 200
        IPDict[request.remote_addr][0] = IPDict[request.remote_addr][0] + 1

    json_data = request.get_json()

    json_response = checkpassword(json_data['name'], json_data['pwHash'])
    return json_response, 200

@app.route('/api/chat/getupdate', methods=['POST'])
@cross_origin()
def getupdate():
    json_data = request.get_json()

    isVaildRequest = checkpassword(json_data['name'], json_data['pwHash'])
    if isVaildRequest['isvalid'] == False:
        return isVaildRequest, 200

    conn = get_db_connection()
    sql_select_query = """select * from chat where postId = ?"""
    chats = conn.execute(sql_select_query, (json_data['postId'],)).fetchall()
    conn.close()

    return chats, 200

@app.route('/api/chat/send', methods=['POST'])
@cross_origin()
def chat():
    json_data = request.get_json()

    isVaildRequest = checkpassword(json_data['name'], json_data['pwHash'])
    if isVaildRequest['isvalid'] == False:
        return isVaildRequest, 200

    conn = get_db_connection()
    conn.execute("INSERT INTO chat (postId, userId, name, content) VALUES (?,?,?,?)",
                (json_data['postId'], json_data['userID'], json_data['name'], json_data['content'])
                )
    conn.commit()
    conn.close()
    
    return jsonify({"send":True}), 200

@app.route('/api/account/updateProfile', methods=['POST'])
@cross_origin()
def changePassword():
    json_data = request.get_json()
    
    isVaildRequest = checkpassword(json_data['name'], json_data['oldpwHash'])
    if isVaildRequest['isvalid'] == False:
        return isVaildRequest, 200

    hash = generate_password_hash(json_data['newpwHash'])
    conn = get_db_connection()
    conn.execute("UPDATE users SET name=?, email=?, pwHash=? WHERE id=?",
                (json_data['newname'], json_data['newemail'], hash, json_data['userID'])
                )
    conn.commit()
    sql_select_query = """select * from users where name = ?"""
    user = conn.execute(sql_select_query, (json_data['name'],)).fetchone()
    conn.close()
    
    user["pwHash"] = json_data['newpwHash']
    json_data = {
        "isvalid":True, "from client": request.remote_addr,
        "User info": user}
    return jsonify(json_data), 200

if __name__ == "__main__":
    app.run()
