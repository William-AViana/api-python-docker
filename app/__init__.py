from flask import Flask
from app import routes

app = Flask(__name__)

@app.route('/')
def home():
    return "hello, world!"

@app.route('/books', method=['GET'])
def get_books():
    return {"books":[]}