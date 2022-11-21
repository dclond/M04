"""
David Clond
SDEV 220 M04 Lab - Case Study: Python APIs
clond_m04_lab_case_study_python_APIs.py


Instructions
Complete the following steps:

    After watching the video, create a CRUD API for a Book instead of a book in the video example above.  The Book model should have the following parameters:
        id
        book_name
        author
        publisher

"""

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book_data.db'
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120))
    publisher = db.Column(db.String(80))

    def __repr__(self):
        return f"{self.book_name} - {self.author} - {self.publisher}"


@app.route('/')
def index():
    return 'Hello!'

@app.route('/books')
def get_books():
    books = Book.query.all()
    
    output = []
    for book in books:
        book_data = {'book_name': book.book_name, 'author': book.author, 'publisher': book.publisher}
        output.append(book_data)
    return {"books": output}

@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {"book_name": book.book_name, "author": book.author, "publisher": book.publisher}

@app.route('/books', methods=['POST'])
def add_book():
    book = Book(book_name=request.json['book_name'], author=request.json['author'], publisher=request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}

@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"error": "not fournd"}
    db.session.delete(book)
    db.session.commit()
    return {"message": "yeet!@"}

