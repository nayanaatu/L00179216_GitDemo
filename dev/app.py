from flask import Flask, redirect, url_for, request
app = Flask(__name__)


@app.route('/hello_msg/<name>')
def hellow_msg(name):
    return f"HELLO, WELCOME TO ATU LETTERKENNY UNIVERSITY {name}!!!"


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        var = redirect(url_for('hello_msg', name=user))
        print("return val : ", var)
        return var
    else:
        user = request.args.get('nm')
        return redirect(url_for('hello_msg', name=user))


if __name__ == '__main__':
    app.run(debug=True)

