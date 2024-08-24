from flask import Flask,json
from flask import request
from flask_cors import  CORS
from db import response_insert,get_access_token
app = Flask(__name__)
CORS(app)
@app.route("/insert_response",methods=['POST'])
def insert_response():
    data = request.get_json()
    json_data = json.dumps(data["body"])
    code = response_insert(json_data)
    print(code)
    return code,200

@app.route("/get_access_token",methods=['GET'])
def access_token():
    token = get_access_token()
    return token, 200
app.run(host="0.0.0.0",debug=False)
