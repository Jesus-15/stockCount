"""
file - Stock Count
author - Jesus Pombo
description - Stock count page.
"""

from flask import Flask, render_template, request, make_response, jsonify, send_file
import json

app = Flask(__name__)


# @app.route('/')
# def stock_count_page():
#     """
#     function stock_count_page() - This function is used to render the original page the warehouse operative will see,
#     with empty data fields.
#     """
#     return render_template('index.html')


@app.route('/')
def inventory_read():

    with open('data/inventory.json', 'r') as file:
        data = file.read()
        json_data = json.loads(data)
        file.close()
        return json_data


if __name__ == '__main__':
    app.run()
