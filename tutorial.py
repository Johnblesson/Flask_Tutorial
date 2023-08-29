from flask import Flask, redirect, url_for

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return "Hello! This is the main page <h1>HELLO</h1>"

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

# Redirection
@app.route("/admin")
def admin():
    return redirect(url_for("home"))

# Starting the server
if __name__ == "__main__":
    app.run()