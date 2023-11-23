#/usr/local/bin/python3

from flask import Flask
from termcolor import colored

app = Flask(__name__)

@app.route("/")
def hellow_msg():
    """
    Method to return hello message
    """
    text = colored("HELLO, WELCOME TO ATU LETTERKENNY UNIVERSITY!!!", 'green', attrs=['reverse', 'blink'])
    return text


def student_postgraduate(student_label_number):
    """
    Method to check students grade level
    """
    if student_label_number == 9:
        return f"Welcome Postgraduate Students"
    else:
        return f"Welcome Graduate Students"


if __name__ == "__main__":
    app.run()
