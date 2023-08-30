#!/usr/bin/env python3

from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/<name>")
def home(name):
    return render_template("0-index.html", content=["John", "Kharis", "Blesson"])

if __name__ == "__main__":
    app.run(debug=True)