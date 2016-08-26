# coding: utf-8

from flask import (
    Flask,
    jsonify,
    request,
)
from flask_cors import CORS

from pyshell import (
    run_shell,
    run_source,
)

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return jsonify(msg='welcome to pyshell server')


@app.route('/run/shell', methods=['POST'])
def run_pyshell():
    code = request.json.get('code', '')
    ret = run_shell(code)
    return jsonify(ret=ret)


@app.route('/run/source', methods=['POST'])
def run_pysource():
    code = request.json.get('code', '')
    ret = run_source(code)
    return jsonify(ret=ret)


if __name__ == '__main__':
    app.run(debug=True)
