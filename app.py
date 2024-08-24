from flask import Flask
from flask import request
from flask_cors import  CORS
from db import response_insert,get_access_token
app = Flask(__name__)
CORS(app)
@app.route("/insert_response",methods=['POST'])
def insert_response():
    data = request.get_json()
    code = response_insert(data)
    return code
@app.route("/get_access_token",methods=['GET'])
def access_token():
    token = get_access_token()
    return token, 200
app.run(host="0.0.0.0",debug=False)
