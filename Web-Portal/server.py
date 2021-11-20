from flask import Flask, render_template
from controllers import *

app = Flask(__name__)


@app.route('/')
def connection():
    return render_template('connection.html')


@app.route('/connection')
def connection2():
    return render_template('connection.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
