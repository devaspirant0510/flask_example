from flask import Flask, redirect, url_for


app=Flask(__name__)
a=False
@app.route('/')
def home():
	return "플라스크 웹페이지 <h1>헬로월드</h1>"

@app.route("/<name>")
def user(name):
	return f"안녕{name}!"

@app.route("/admin")
def admin():
	if a:
		return redirect(url_for("home"))
	else:
		return "gg"
if __name__ == '__main__':
	app.run(host='192.168.0.5')