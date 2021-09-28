from flask import Flask, jsonify, request

app = Flask(__name__)

book_catalogue =  [
    {
        'name': 'Harry Potter 1',
        'genre': 'Fantasy',
        'author': 'JK Rowling'
    }
]


@app.route('/books')
def get_all_books():
    return jsonify({'book_catalogue': book_catalogue})



@app.route('/books/<string:name>')
def get_each_book(name):
    pass


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

if __name__ == '__main__':
    app.run(debug=True, port = 5001, host = '0.0.0.0')
