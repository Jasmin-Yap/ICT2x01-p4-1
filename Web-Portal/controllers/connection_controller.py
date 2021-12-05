from models.connection import Connection
from controllers import connection_controller, token_controller, maze_controller
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
instruction_page = Blueprint('instruction_page', __name__)


@connection_page.route('/connection', methods=['GET', 'POST'])
def connectionPage():
    token_controller.check_token()
    if request.method == 'POST':
        conn.set_ip(request.form['ipInput'])
        conn.set_port(request.form['portInput'])

        address = "http://" + conn.get_ip() + ":" + conn.get_port() + "/"
        testDat = {'ISN': 0, 'TOK': token_controller.get_token(), 'E': '#'}
        r = requests.post(address, testDat)
        #print(token_controller.get_token())
        #print(r.status_code)

        if r.status_code == 200:
            r = requests.get(address, params={"type": "T"})
            #Token = token_controller.get_token()
            #print(r.text)
            #print(Token)
            if token_controller.verify_token(r.text):
                #print("Verified")
                return render_template('dashboard.html')

    conn_details = connection_controller.get_address()
    disconnect()
    token_controller.clear_token()
    maze_controller.clear_custom_mazes()
    return render_template('connection.html', address=conn_details)


'''
def end_session():
    token_controller.clear_token()
    maze_controller.clear_custom_mazes()
    return render_template('connection.html')
'''


@instruction_page.route('/instruction', methods=['GET', 'POST'])
def instructionPage():
    if request.method == 'POST':
        address = "http://" + conn.get_ip() + ":" + conn.get_port() + "/"
        testDat = {'ISN': 1, 'Direction': 'l', 'TOK': token_controller.get_token(), 'E': '#'}
        r = requests.post(address, testDat)
        print(token_controller.get_token())
        print(r.status_code)

        if r.status_code == 200:
            r = requests.get(address, params={"type": "T"})
            Token = token_controller.get_token()
            print(r.text)
            print(Token)
            if token_controller.verify_token(r.text):
                print("Verified")

        return render_template('dashboard.html')
