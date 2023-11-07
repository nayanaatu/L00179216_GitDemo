from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "WELCOME TO ATU LETTERKENNY UNIVERSITY!!!"

if __name__ == "__main__":
    app.run()
