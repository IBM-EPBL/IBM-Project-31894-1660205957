from flask import Flask, render_template

app = Flask(__name__,template_folder='template')

@app.route("/login") 
def hello_world():
    return render_template('login.html')

@app.route("/index") 
def hello():
    return render_template ('bootstrap.html')




@app.route("/home")
def home():
    return "<p>hello,world!</p>"


@app.route("/about")
def about():
    return "<p>hello about homepage</p>"