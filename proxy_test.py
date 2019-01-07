from flask import Flask, request, jsonify
import requests
cardURL = "https://auth.uwamakers.com/api/card"
token = "m7cGBbGflbJUGijdA7MrDBPStFxVHGKp9Ep4Z2sfKSk6"

def uidSplitter(uid):
    uid = str(uid)
    uid = uid.replace("b'", "").replace("'", "")
    byteArray = []
    for i in range(1,8,2):
        byte = int(uid[i-1 : i+1], 16)
        byteArray.append(byte)
    return(byteArray)

def checkPermission(username, perm):
    permURL = "https://auth.uwamakers.com/api/users/?perm=" + perm + "&token=" + token
    permRequest = requests.get(permURL)
    userList = permRequest.text
    if(username in userList):
        return(True)
    return False

app = Flask(__name__)
@app.route("/post", methods = ["POST"])
def post():
    uid = request.data
    byteArray = uidSplitter(uid)
    PARAMS = {"token" : token, "uuid": byteArray}
    detailsRequest = requests.post(url = cardURL, params = PARAMS)
    response = detailsRequest.json()
    username = response['user']['username']
    status = checkPermission(username, "joining.joined")
    print(status)
    return(jsonify(status))




app.run(host="0.0.0.0", port = 8090)




