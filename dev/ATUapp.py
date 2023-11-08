from flask import Flask, redirect, url_for, request
app = Flask(__name__)


@app.route('/<name>')
def hello_msg(name):
	return f"HELLO, WELCOME TO ATU LETTERKENNY UNIVERSITY {name}!!!"


@app.route('/login', methods=['POST', 'GET'])
def login():
	if request.method == 'POST':
        user = request.form['nm']
        var = redirect(url_for(name=user))
        print("retrun val : ", var)
        return var
	else:
		user = request.args.get('nm')
		return redirect(url_for(name=user))


if __name__ == '__main__':
	app.run(debug=True)

