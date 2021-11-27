from models.connection import Connection
from flask import Flask, render_template, request, redirect, url_for, Blueprint
import requests

conn = Connection()


def connect_to_car(ip, port):
    conn.set_ip(ip)
    conn.set_port(port)


def verify_address():
    # server.logging.debug(self.auth_token.get_code())
    # server.logging.debug(code)
    details = [conn.get_ip(), conn.get_port()]
    return details


def disconnect():
    conn.set_ip("0.0.0.0")
    conn.set_port("0")


connection_page = Blueprint('connection_page', __name__)


@connection_page.route('/connection', methods=['GET', 'POST'])
def connectionPage():
    i = 0
    Token = 'a1b2c3'
    if request.method == 'POST':
        address = "http://" + request.form['ipInput'] + ":" + request.form['portInput'] + "/"
        #testDat = {'ISN': 0, 'TOK': 'a1b2c3', 'E': '#'}
        testDat = {'ISN': 1, 'Speed': 10, 'Distance': 5, 'TOK': Token, 'E': '#'}
        r = requests.post(address, testDat)
        if r.status_code == 200:
            r = requests.get(address, params={"type": "T"})
            if r.text == Token:
                connect_to_car(request.form['ipInput'], request.form['portInput'])
                details = verify_address()
                conn_details = {
                    'ip': details[0],
                    'port': details[1]
                }
        return render_template('connection.html', address=conn_details)
    else:
        disconnect()
        details = verify_address()
        conn_details = {
            'ip': details[0],
            'port': details[1]
        }
        return render_template('connection.html', address=conn_details)
