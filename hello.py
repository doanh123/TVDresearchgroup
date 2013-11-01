import os
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index')
def mainpage():
    return render_template('indx.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/membership')
def membership():
    return render_template('membership.html')

@app.route('/publication')
def publication():
    return render_template('publication.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/login', methods =['POST'])
def login():
    if request.method == "POST":
        if request.form['username'] == "foo" and request.form['password'] == "bar":
            return render_template("welcome.html")

    return "WRONG PASSWORD"
