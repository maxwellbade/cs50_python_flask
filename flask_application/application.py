from flask import Flask, render_template, request, session
from flask_session import Session
import datetime

#this app is __name__
app = Flask(__name__)

#load flask
#first export FLASK_APP=application.py
#FLASK_DEBUG=1
#export FLASK_ENV=development
#flask ren
#FLASK_APP=application.py FLASK_DEBUG=1 FLASK_ENV=development flask run

#kill process:
#ps -fA | grep python to see all python services running
#kill -9 id to kill
#restart shell

#app config for sessions
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/") #default page
def index():
    return "Hello, World!"

@app.route("/max") #max page
def max():
    return "Hello, Max!"

@app.route("/andi") #max page
def andi():
    return "Hello, Andi!"

@app.route("/<string:name>") #any name
def hello(name):
    name = name.upper()
    return f"<h1>Hello, {name}!</h1>"

@app.route("/")
def template():
    headline = "This is the Headline"
    return render_template("index.html", headline=headline)

@app.route("/bye")
def bye():
    headline = "Goodbye!"
    return render_template("index.html", headline=headline)

@app.route("/newyear")
def newyear():
    now = datetime.datetime.now()
    newyear = now.month == 1 and now.day == 1
    #newyear = True
    return render_template("index.html", newyear=newyear)

@app.route("/names")
def names():
    names = ["Max","Andi","Carol","Sarah","Ben","Joey"]
    return render_template("names.html",names=names)

@app.route("/lorem")
def lorem():
    return render_template("lorem.html")

@app.route("/more")
def more():
    return render_template("more.html")

@app.route("/layout")
def layout():
    return render_template("layout.html")

@app.route("/layout_index")
def layout_index():
    return render_template("layout_index.html")

@app.route("/layout_more")
def layout_more():
    return render_template("layout_more.html")


@app.route("/form_index")
def form_index():
    return render_template("form_index.html")

@app.route("/form_hello", methods=["GET", "POST"])
def form_hello():
    if request.method == "GET":
        return "Please submit the form instead."
    else :
        name = request.form.get("name")
        return render_template("form_hello.html", name=name)

notes = []

@app.route("/notes", methods=["GET", "POST"])
def notes():
    if session.get("notes") is None:
        session["notes"] = []
    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)

    return render_template("notes.html", notes=session["notes"])
