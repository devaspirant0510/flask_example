from flask import Flask, redirect, url_for, render_template
from flask import request,session,flash
from datetime import timedelta
from datetime import datetime

app = Flask(__name__)
app.secret_key = "fgfhgjdfj5675467fdg345dsfg"
app.parmanent_session_lifetime = timedelta(seconds=5)
@app.route("/")
def home():
	return render_template("index.html")

@app.route("/login", methods=['POST','GET'])
def login():
	if request.method == 'POST':
		session.parmanent=True
		user = request.form["nm"]
		session['user'] = user
		return redirect(url_for("user"))
	else:
		if "user" in session:
			return redirect(url_for("user"))
		return render_template("login.html")

@app.route("/user")
def user():
	if "user" in session:
		user = session["user"]
		return f"<h1>{user}안녕</h1>{datetime.now()}"
	else:
		return redirect(url_for("login"))

@app.route("/logout")
def logout():
	print(session)
	session.pop("user", None)
	return redirect(url_for("login"))
if __name__ == '__main__':
	app.run(host='192.168.0.5',debug=True)