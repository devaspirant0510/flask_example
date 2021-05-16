from flask import Flask
import math
app=Flask(__name__)
@app.route("/")
def hello():
   return "<h1>hello</h1><br><a href=http://www.naver.com>네이버 </a>"

@app.route("/hh/<name>")
def name(name):
   return "hello %s"%name
@app.route("/int/<int:post_id>")
def show_int(post_id):
   return 'Post : %d'%post_id
@app.route("/math/<float:math_PI>")
def mathpi(math_PI):
   return 'PI : %f'%math.pi
if __name__ == "__main__":
   app.run()
