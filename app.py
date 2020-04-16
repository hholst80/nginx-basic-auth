from flask import Flask, request

app = Flask(__name__)

@app.route("/auth")
def auth():
    noo = "ACCESS DENIED", 403
    yes = "OK", 200

    if not request.authorization:
        return noo

    username = request.authorization["username"]
    password = request.authorization["password"]

    if username != 'foo' or password != 'bar':
        return noo

    # I'm sure it's bad practice to authorize in the otherwise path. ;-)
    return yes
