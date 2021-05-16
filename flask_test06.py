from flask import Flask, redirect, url_for, render_template
from flask import request,session,flash
from datetime import timedelta
from datetime import datetime
from flask_sqlalchemy import  SQLAlchemy

app = Flask(__name__)
app.secret_key = "fgfhgjdfj5675467fdg345dsfg"
app.config['SQLAlchemy_DATABASE_URI'] = 'sqlite://users.sqlite3'
app.config['SQLAlchemy_TRACK_MODIFICATIONS']=False
app.parmanent_session_lifetime = timedelta(seconds=5)


db = SQLAlchemy(app)

class user(db.Model):
	_id = db.Column("id", db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	email =db.Column(db.String(100))

	def __init__(self, name, email):
		self.name = name
		self.email = email




@app.route("/")

def home():
	return render_template("index.html")

@app.route("/login", methods=['POST','GET'])
def login():
	if request.method == 'POST':
		session.parmanent=True
		user = request.form["nm"]
		session['user'] = user
		
		found_usr = users.query.filter_by(name=user).first()
		if found_usr:
			session['email']=found_user.email
		else:
			usr = users(user, "")
			db.session.add(usr)
			db.commit()

		flash("login succesful")
		return redirect(url_for("user"))
	else:
		if "user" in session:
			flash("Already Logged In!")
			return redirect(url_for("user"))
		return render_template("login.html")

@app.route("/user", methods=['POST','GET'])
def user():
	email=None
	if 'user' in session:
		user = session["user"]
		if request.method == 'POST':
			email = request.form['email']
			session['email']=email
			found_usr = users.query.filter_by(name=user).first()
			found_usr.email = email
			db.commit()
			flash("Email was saved!")
		else:
			if 'email' in session:
				email = session['email']

		return render_template("user.html",email=email)
	else:
		flash("You are not logged out!")
		return redirect(url_for("login"))

@app.route("/logout")
def logout():

	flash(f"you have been logged out!,{user}","info")
	session.pop('user', None)
	session.pop('email',None)
	return redirect(url_for("login"))
if __name__ == '__main__':
	db.create_all()
	app.run(host='192.168.0.5',debug=True)