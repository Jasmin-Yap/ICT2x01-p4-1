from models.connection import Connection
from flask import Flask, render_template, redirect, url_for, request
import socket


app = Flask(__name__)

conn = Connection()


def connect_to_car(ip, port):
    conn.set_ip(ip)
    conn.set_port(port)
    return verify_address()


def verify_address():
    # server.logging.debug(self.auth_token.get_code())
    # server.logging.debug(code)
    return conn.get_ip() + ":" + connection.get_port()


def disconnect():
    conn.set_ip("0.0.0.0")
    conn.set_port("0")
    return verify_address()


@app.route('/connection2', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        host = request.form['ipInput']
        port = request.form['portInput']
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.sendall(b'Hello, world')
        data = s.recv(1024)
        s.close()
        print('Received', repr(data))

        #ip = request.form['ipInput']
        #port = request.form['portInput']
        #render_template('dashboard.html')

        return render_template('dashboard.html')
    else:
        return render_template('dashboard.html')
