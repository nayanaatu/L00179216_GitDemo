#/usr/local/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hellow_msg():
    """
    method to return hello message
    """
    return "HELLO, WELCOME TO ATU LETTERKENNY UNIVERSITY!!!"

if __name__ == "__main__":
    app.run()
