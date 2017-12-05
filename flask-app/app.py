from flask import Flask
from flask import render_template
from required_courses import generateText
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", text=generateText())
