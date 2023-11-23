#/usr/local/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hellow_msg():
    """
    Method to return hello message
    """
    print("\033[1;32m This text is Bright Green  \n")
    return f"\033[1;32m HELLO, WELCOME TO ATU LETTERKENNY UNIVERSITY!!! \n"

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
