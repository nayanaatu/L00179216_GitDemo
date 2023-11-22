#/usr/local/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hellow_msg():
    """
    Method to return hello message
    """
    return "HELLO, WELCOME TO ATU LETTERKENNY UNIVERSITY!!!"

def student_postgraduate(student_label_number):
    if student_label_number == 9:
        return f"Welcome postgraduate students"
    else:
        return f"Welcome graduate students"


if __name__ == "__main__":
    app.run()
