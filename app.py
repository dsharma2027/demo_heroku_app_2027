from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Learning Heroku in Praxis"

@app.route('/someendpoints')
def firstendpoint():
    return "This is my first path on Heroku"

if __name__ == "main":
    app.run()


