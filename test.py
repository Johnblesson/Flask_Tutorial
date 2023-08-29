from flask import Flask

app = Flask(__name__)

# Home Route
@app.route('/about')
def about():
    return "This is the test about page"

if __name__ == "__main__":
    app.run()