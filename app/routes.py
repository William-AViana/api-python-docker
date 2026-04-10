from app import app
from flask import request

@app.route('/')
def home():
    return "hello, world!"

livros = [
    {'id': 1, 'titulo': 'O Senhor dos Anéis', 'autor': 'J.R.R. Tolkien'},
    {'id': 2, 'titulo': 'Harry Potter', 'autor': 'J.K. Rowling'}
]

@app.route('/books', methods=['GET'])
def get_books():
    return {"books":livros}

@app.route('/books', methods=['POST'])
def post_books():
    new_book = request.get_json()
    livros.append(new_book)
    return new_book, 201