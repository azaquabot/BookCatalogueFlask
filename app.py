from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://root:root@44.142.109.4:5432/book_catalogue"
db = SQLAlchemy(app)

Book_Genre = db.Table('book_genre',
                      db.Column('book_id', db.Integer, db.ForeignKey('genre.id'), primary_key=True),
                      db.Column('genre_id', db.Integer, db.ForeignKey('book.id'), primary_key=True)
                      )

class Genre(db.Model):
    __tablename__ = "genre"
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String, unique=True, nullable=False)

    def __repr__(self):
        return f'<Genre {self.name!r}>'


class Author(db.Model):
    __tablename__ = "author"
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String, unique=True)
    age = db.Column(db.Integer, index=False)

    def __repr__(self):
        return f'<User {self.name!r}>'


class Book(db.Model):
    __tablename__ = "book"
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String, unique=True, index=True)
    price = db.Column(db.String, unique=True, index=True)
    description = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    author = db.relationship('Author', foreign_keys=author_id)
    genres = db.relationship('Genre', secondary=Book_Genre, lazy='subquery',
                             backref=db.backref('books', lazy=True))

    def __repr__(self):
        return f'Person(name={self.name}, age={self.price}, age={self.description},age={self.author}, age={self.genre})'


book_catalogue = [
    {
        'name': 'Harry potter 2',
        'genre': 'Fantasy',
        'author': 'JK Rowling'
    }
]


# Produce a list of all the books with their authors and genres.
# GET
# /books/
@app.route('/books', methods=['GET'])
def get_all_books():
    books = Book.query.all()
    results = [book._asdict() for book in books]

    return jsonify({"count": len(results), "books": results})


# Give details of each and every book with its author and the genres.
# GET
# /books/<string:name>
@app.route('/books/<string:name>')
def get_each_book(name):
    pass


# Provide the support for creating, updating and deleting a book.
# POST							
# /books/<string:name>/book {name:, genre:, author}	
@app.route('/books', methods=['POST'])
def create_book():
    request_data = request.get_json()
    new_book = {
        'name': request_data['name'],
        'author': request_data['author'],
        'genre': request_data['genre']
    }
    book_catalogue.append(new_book)
    return jsonify(new_book)


# PUT
# /books/<string:name>/book {name:, genre:, author}	

# DELETE
# /books/<string:name>/book {name:, genre:, author}


# Produce a list of all the authors with their books published.
# GET
# /authors/
@app.route('/authors', methods=['GET'])
def get_all_authors():
    authors = Author.query.all()
    results = [
        {
            "name": author.name,
            "age": author.age
        } for author in authors]
    return jsonify(results)

# Details of each and every author with their published books.
# GET
# /authors/<string:name>
@app.route('/authors/<string:name>')
def get_each_author(name):
    #name = request.args.get('name', default ='*', type = str)
    authors = Author.query.filter_by(name=name).first()
    results = [
        {
            "name": author.name,
            "age": author.age
        } for author in authors]

    return jsonify({"author": results})

# Provide the support for creating, updating and deleting an author.
# POST					
# /authors/<string:name>/author {name:}
@app.route('/authors', methods=['POST'])
def post_author():
    if request.is_json:
        data = request.get_json()
        new_author = Author(name=data['name'], age=data['age'])
        db.session.add(new_author)
        db.session.commit()
        return {"message": f"author {new_author.name} has been created successfully."}
    else:
        return {"error": "The request payload is not in JSON format"}
# PUT
# /authors/<string:name>/author {name:}	

# DELETE
# /authors/<string:name>/author {name:}

# Produce a list of all the genres and the respective books in each genre.
# GET
# /genres/
@app.route('/genres', methods=['GET'])
def get_all_genres():
    genres = Genre.query.all()
    results = [
        {
            "name": genre.name
        } for genre in genres]
    return jsonify(results)

# Each genre and the books that fall into this genre.
# GET
# /genres/<string:name>
@app.route('/genres/<string:name>')
def get_each_genre(name):
    #name = request.args.get('name', default ='*', type = str)
    genres = Genre.query.filter_by(name=name).first()
    results = [
        {
            "name": genre.name
        } for genre in genres]

    return jsonify({"genre": results})

# Provide the support for creating, updating and deleting a genre.
# POST
# /genres/<string:name>/genre {name:}	
@app.route('/genres', methods=['POST'])
def post_genre():
    if request.is_json:
        data = request.get_json()
        new_genre = Genre(name=data['name'])
        db.session.add(new_genre)
        db.session.commit()
        return {"message": f"genre {new_genre.name} has been created successfully."}
    else:
        return {"error": "The request payload is not in JSON format"}

# PUT
# /genres/<string:name>/genre {name:}			

# DELETE
# /genres/<string:name>/genre {name:}


if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')
