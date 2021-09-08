import flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello_world():
    return render_template('0-index.html')