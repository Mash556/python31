from flask import Flask, jsonify, request
from main import *

app = Flask(__name__)

@app.route('/create/', methods=['POST'])
def create_item_rq():
    data = request.get_json()
    item = ItemPydantic(
        title = data.get('title', 'no title'),
        author = data.get('author', 'no author'),
        genre = data.get('genre', 'no genre'),
        created_at = data.get('created_at', 'no date')
    )
    create(item)
    return jsonify({'message': 'created successfully'})



@app.route('/read/', methods=['GET'])
def get_items():
    items = read()
    return jsonify({'data':items})


@app.route('/read_one/<int:id_>/', methods=['GET'])
def get_one_items(id_):
    items = read_one(id_)
    if not items:
        return jsonify({'message': 'not found'})
    return jsonify({'data':items})


@app.route('/update/<int:id_>/', methods=['PUT'])
def update_items(id_):
    try:
        data = request.get_json()
        item = ItemPydantic(
        title = data.get('title', 'no title'),
        author = data.get('author', 'no author'),
        genre = data.get('genre', 'no genre'),
        created_at = data.get('created_at', 'no date')
    )
        update(id_, item)
        return 'Update Successfully'
    except:
        return "Data was a uncoorrect"


@app.route('/delete/<int:id_>/', methods=['DELETE'])
def delete_items(id_):
    items = delete(id_)
    return f'Столбец под идентификатором {id_} успешно удалился.'


app.run(host='localhost', port=8000)
