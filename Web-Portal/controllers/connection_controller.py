from models.connection import Connection
import controllers.token_controller
from flask import Flask, render_template, request, redirect, url_for, Blueprint
import requests

conn = Connection()


def connect_to_car(ip, port):
    conn.set_ip(ip)
    conn.set_port(port)


def get_address():
    # server.logging.debug(self.auth_token.get_code())
    # server.logging.debug(code)
    return {'ip': conn.get_ip(), 'port': conn.get_port()}


def disconnect():
    conn.set_ip("0.0.0.0")
    conn.set_port("0")


connection_page = Blueprint('connection_page', __name__)


@connection_page.route('/connection', methods=['GET', 'POST'])
def connectionPage():
    #i = 0
    #Token = 'a1b2c3'
    token_controller.generate_token()
    if request.method == 'POST':
        address = "http://" + request.form['ipInput'] + ":" + request.form['portInput'] + "/"
        testDat = {'ISN': 0, 'TOK': token_controller.auth_token.get_token(), 'E': '#'}
        #testDat = {'ISN': 1, 'Speed': 10, 'Distance': 5, 'TOK': Token, 'E': '#'}
        r = requests.post(address, testDat)
        if r.status_code == 200:
            r = requests.get(address, params={"type": "T"})
            if token_controller.verify_token(r.text):
                print("Verified")
        return render_template('dashboard.html')
    else:
        disconnect()
        conn_details = get_address()
        return render_template('connection.html', address=conn_details)
