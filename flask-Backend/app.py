import os
import socket
from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome Python flask!"

@app.route('/api/about')
def about():
    return 'I am '+socket.gethostname()

@app.route('/api/users')
def get_users():
    json_data = [{"name":"alice","age":18},{"name":"bob", "age": 22}]
    return jsonify(json_data),200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True, use_reloader=False)   