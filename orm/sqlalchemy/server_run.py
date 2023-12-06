# API - API(интерфейс програмирование приложение), набор опрределенных правил и инструментов ,
# которые  позволяют приложениям взаимодействовать

# HTTP, SSH, TCP/ip

from flask import Flask, jsonify, request
from main import *

app = Flask(__name__)

@app.route('/get_items/', methods=['GET'])
def get_items():
    items = get_item()
    return jsonify({'data':items})


@app.route('/create_item/', methods=['POST'])
def create_item_rq():
    data = request.get_json()
    item = ItemPydantic(
        name = data.get('name', 'no name'),
        dascription = data.get('dascription', 'no dess'),
        price = data.get('price', 0)
    )
    create_item(item)
    return jsonify({'message': 'created successfully'})



@app.route("/retrieve_item/<int:item_id>/", methods= ['GET'])
def get_one_item(item_id):
    item = retrieve_item(item_id)
    if not item:
        return jsonify({'message': 'not found'})
    return jsonify({'data':item})





@app.route('/', methods=['GET'])
def hello():
    return '<h1>Hello World<h1>'

# update
# delete



@app.route("/update_item/<int:item_id>/", methods= ['PUT'])
def update_item_fk(item_id):
    try:
        data = request.get_json()
        update_item(item_id, data)
        return 'Update Successfully'
    except:
        return "Data was a uncoorrect"



@app.route("/delete_item/<int:item_id>/", methods= ['DELETE'])
def delete(item_id):
    delete_item(item_id)
    return f'успешно'


# if __name__ == '__main__':
#     app.run(debug=True)   

app.run(host='localhost', port=8000)