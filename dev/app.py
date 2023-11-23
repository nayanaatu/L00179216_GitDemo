#/usr/local/bin/python3

from flask import Flask
from colorama import init, Fore, Back, Style

init()

# all available foreground colors
FORES = [ Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE ]
# all available background colors
BACKS = [ Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE ]
# brightness values
BRIGHTNESS = [ Style.DIM, Style.NORMAL, Style.BRIGHT]

app = Flask(__name__)

#@app.route("/")
def hellow_msg():
    """
    Method to return hello message
    """
    return "HELLO, WELCOME TO ATU LETTERKENNY UNIVERSITY!!!"

def student_postgraduate(student_label_number):
    if student_label_number == 9:
        return f"Welcome Postgraduate Students"
    else:
        return f"Welcome Graduate Students"

@app.route("/")
def print_with_color(s, color=Fore.WHITE, brightness=Style.NORMAL):
    """Utility function wrapping the regular `print()` function 
    but with colors and brightness"""
    return(f"{brightness}{color}{s}{Style.RESET_ALL}")

for fore in FORES:
    for brightness in BRIGHTNESS:
        print_with_color("HELLO, WELCOME TO ATU LETTERKENNY UNIVERSITY!!!", color=fore, brightness=brightness)


if __name__ == "__main__":
    app.run()
