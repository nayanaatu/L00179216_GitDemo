from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_msg():
    return "HELLO, WELCOME TO ATU LETTERKENNY UNIVERSITY!!!"

if __name__ == "__main__":
    app.run()
