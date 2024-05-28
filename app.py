from flask import Flask, render_template, Request, redirect, session
import json
import os

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/users")
def users():
    return render_template("users.html")

@app.route("/customers")
def customers():
    return render_template("customers.html")

@app.route('/register')
def register():
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)