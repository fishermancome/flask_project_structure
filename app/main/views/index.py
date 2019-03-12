from flask import jsonify
from app.main import main


@main.route('/index/', methods=['GET'])
def index():
    return jsonify({
        "hello": "world"
    })
