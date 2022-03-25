"""
file - Stock Count
author - Jesus Pombo
description - Stock count page.
"""

from flask import Flask, render_template, request, make_response, jsonify

app = Flask(__name__)


@app.route('/')
def stock_count_page():
    """
    function stock_count_page() - This function is used to render the original page the warehouse operative will see,
    with empty data fields.
    """
    return render_template('index.html')


def user_allocation():
    """
    function user_allocation() - This function is used to grab the username entered, and then initialise all of the
    blank variables to be filled in.
    """
    username = ""


def inventory():
    name = 0


if __name__ == '__main__':
    app.run()
