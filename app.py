"""
file - Stock Count
author - Jesus Pombo
description - Stock count page.
"""

from flask import Flask, render_template, request, make_response, jsonify, send_file, redirect, url_for
import json

app = Flask(__name__)


@app.route('/')
def stock_count_page():
    """
    function stock_count_page() - This function is used to render the original page the warehouse operative will see,
    with empty data fields.
    """
    return render_template('index.html')


@app.route('/read', methods=['GET'])
def inventory_read():

    if request.method == 'GET':
        with open('data/inventory.json', 'r') as file:
            data = file.read()
            # json_data = json.loads(data)

            response = make_response(
                jsonify(
                    {"result": data}
                ),
                200,
            )
            file.close()

            response.headers["Content-Type"] = "application/json"

            return response


@app.route('/api/delete', methods=['GET', 'PUT'])
def delete_from_inventory():
    if request.method == "GET":
        sku = str(request.args.get('sku'))

        filename = "data/inventoryRestricted.json"
        filename2 = "data/inventory.json"

        with open(filename, "r") as f:
            data = json.load(f)

        # position of item to change
        current = 0

        # delete item from inventoryRestricted if match found
        for i in data['inventory']:
            if i['sku'] == sku:
                del data['inventory'][current]
            current += 1

        # write to file
        with open(filename, "w") as f:
            json.dump(data, f)


        with open(filename2, "r") as f2:
            data2 = json.load(f2)

        current = 0

        for i in data2['inventory']:
            if i['sku'] == sku:
                del data2['inventory'][current]
            current += 1

        with open(filename2, "w") as f:
            json.dump(data2, f)
    return data


@app.route('/api/add', methods=['GET', 'PUT'])
def add_count_to_inventory():
    if request.method == "GET":
        # get item details from url
        sku = str(request.args.get('sku'))
        count = str(request.args.get('count'))

        filename = "data/inventoryRestricted.json"
        filename2 = "data/inventory.json"

        with open(filename, "r") as f:
            data = json.load(f)

        with open(filename2, "r") as f2:
            data2 = json.load(f2)

        # position of item to change
        current = 0

        # delete item from inventoryRestricted if match found
        for i in data['inventory']:
            if i['sku'] == sku:
                data2['inventory'].append(data['inventory'][current])
            current += 1
        current = 0
        for j in data['inventory']:
            if j['sku'] == sku:
                del data['inventory'][current]
            current += 1

        # write to file
        with open(filename, "w") as f:
            json.dump(data, f)

        current = 0

        for i in data2['inventory']:
            if i['sku'] == sku:
                data2['inventory'][current]['count'] = count
            current += 1

        with open(filename2, "w") as f:
            json.dump(data2, f)
    return data


@app.route('/api/add_item', methods=['GET', 'PUT'])
def add_item_to_inventory_restricted():
    if request.method == "GET":
        # get item details from url
        sku = str(request.args.get('sku'))
        description = str(request.args.get('description'))
        location = str(request.args.get('location'))

        unique = True

        filename = "data/inventoryRestricted.json"

        with open(filename, "r+") as f:
            data = json.load(f)

        inventory = data['inventory']
        new_item = {'sku': sku, 'description': description, 'location': location, 'count': ""}

        for i in data['inventory']:
            if i['sku'] == sku:
                unique = False

        if unique:
            inventory.append(new_item)

        with open(filename, 'w') as f:
            json.dump(data, f)

        return data


if __name__ == '__main__':
    app.run()
