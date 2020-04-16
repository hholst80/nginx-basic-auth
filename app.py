from flask import Flask, request

app = Flask(__name__)

@app.route("/auth")
def auth():
    noo = "ACCESS DENIED\r\n", 403
    yes = "OK\r\n", 200

    if not request.authorization:
        return noo

    username = request.authorization["username"]
    password = request.authorization["password"]

    if username == 'admin' and password == 'admin':
        return yes

    uri = request.headers["X-Original-URI"]

    if uri == '/secret.txt' and username == 'foo' and password == 'bar':
        return yes

    return noo
