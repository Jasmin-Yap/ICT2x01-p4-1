import models.connection as conn_mod
from flask import Flask, render_template, request, redirect, url_for
import requests


app = Flask(__name__)

conn = conn_mod.Connection()


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


@app.route('/connection', methods=['GET', 'POST'])
def form():
    r = requests.post("http://192.168.4.1")
    if request.method == 'POST':
        #address = "http://" + request.form['ipInput'] + ":" + request.form['portInput'] + "/"
        address = "http://192.168.4.1/"
        testDat = {'Speed': 10, 'Distance': 5}
        print(requests.get(address))

        #ip = request.form['ipInput']
        #port = request.form['portInput']
        #render_template('dashboard.html')

        return render_template('dashboard.html')
    else:
        return render_template('dashboard.html')
