from models.connection import Connection
from flask import Flask, render_template, request, redirect, url_for, Blueprint
import requests

conn = Connection()


def connect_to_car(ip, port):
    conn.set_ip(ip)
    conn.set_port(port)
    return verify_address()


def verify_address():
    # server.logging.debug(self.auth_token.get_code())
    # server.logging.debug(code)
    details = [conn.get_ip(), conn.get_port()]
    return details


def disconnect():
    conn.set_ip("0.0.0.0")
    conn.set_port("0")
    return verify_address()


connection_page = Blueprint('connection_page', __name__)


@connection_page.route('/connection', methods=['GET', 'POST'])
def connectionPage():
    if request.method == 'POST':
        address = "http://" + request.form['ipInput'] + ":" + request.form['portInput'] + "/"
        #address = "http://192.168.4.1/"
        testDat = {'Speed': 10, 'Distance': 5}
        #requests.post(address, testDat)

        return render_template('dashboard.html')
    else:
        return render_template('dashboard.html')