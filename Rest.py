#- app.py
#- data.json  (stores items temporarily)

from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated DB (in memory)
items = []

@app.route('/items', methods=['GET'])
def get_all_items():
    return jsonify(items)

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    for item in items:
        if item['id'] == item_id:
            return jsonify(item)
    return jsonify({'error': 'Item not found'}), 404

@app.route('/items', methods=['POST'])
def add_item():
    try:
        data = request.get_json()
        if not isinstance(data, dict) or 'id' not in data or 'name' not in data:
            return jsonify({'error': 'Invalid input'}), 400
        items.append(data)
        return jsonify({'message': 'Item added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({'message': 'Item deleted successfully'}), 200

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    for item in items:
        if item['id'] == item_id:
            item.update(data)
            return jsonify({'message': 'Item updated successfully'}), 200
    return jsonify({'error': 'Item not found'}), 404

@app.route('/items', methods=['DELETE'])
def delete_all_items():
    items.clear()
    return jsonify({'message': 'All items deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)

"""
✅ GET All:

    Method: GET

    URL: http://localhost:5000/items

✅ GET by ID:

    Method: GET

    URL: http://localhost:5000/items/1

✅ POST (Add):o

    Method: POST

    URL: http://localhost:5000/items

    Body > raw > JSON:

{
  "id": 1,
  "name": "Mouse"
}
✅ DELETE All:

    Method: DELETE

    URL: http://localhost:5000/items

⚠️ If You Get Errors:

    Check if you're sending raw JSON and setting header Content-Type: application/json.

    Use request.get_json() — not request.form.
"""