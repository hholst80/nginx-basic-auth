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

    if username == 'foo' and password == 'bar':
        return yes

    return noo
