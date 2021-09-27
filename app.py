from flask import Flask, jsonify, request

app = Flask(__name__)

book_catalogue = [
    {
        'name': 'Harry potter 1',
        'genre': 'Fantasy',
        'author': 'JK Rowling'  
    }
]

#Produce a list of all the books with their authors and genres.
#GET
#/books/
@app.route('/books')
def get_all_books():
    return jsonify({'book_catalogue': book_catalogue})

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

# Details of each and every author with their published books.
# GET
# /authors/<string:name>

# Provide the support for creating, updating and deleting an author.
# POST					
# /authors/<string:name>/author {name:}	

# PUT
# /authors/<string:name>/author {name:}	

# DELETE
# /authors/<string:name>/author {name:}






# Produce a list of all the genres and the respective books in each genre.
# GET
# /genres/

# Each genre and the books that fall into this genre.
# GET
# /genres/<string:name>

# Provide the support for creating, updating and deleting a genre.
# POST
# /genres/<string:name>/genre {name:}	

# PUT
# /genres/<string:name>/genre {name:}			

# DELETE
# /genres/<string:name>/genre {name:}


if __name__ == '__main__':
    app.run(debug = True, port = 5001, host = '0.0.0.0')
