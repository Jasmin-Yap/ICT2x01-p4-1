import sys, logging, gc, copy
from flask import Flask, render_template
from controllers import connection_controller

app = Flask(__name__)
app.register_blueprint(connection_controller.connection_page)


@app.route('/')
def connection():
    details = connection_controller.verify_address()
    conn_details = {
        'ip': details[0],
        'port': details[1]
    }
    return render_template('connection.html', address=conn_details)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
