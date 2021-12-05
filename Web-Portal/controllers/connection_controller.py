from models.connection import Connection
from controllers import connection_controller, token_controller, maze_controller, dashboard_controller
from flask import Flask, render_template, request, Blueprint
import requests
from apscheduler.schedulers.background import BackgroundScheduler


conn = Connection()
# scheduler = BackgroundScheduler()
# scheduler.start()


"""
setting IP and port for connection to robotic car
"""
def connect_to_car(ip, port):
    conn.set_ip(ip)
    conn.set_port(port)


"""
get IP and port for the robotic car
"""
def get_address():
    return {'ip': conn.get_ip(), 'port': conn.get_port()}


"""
clear IP and port
"""
def disconnect():
    conn.set_ip("0.0.0.0")
    conn.set_port("0")
    conn_details = connection_controller.get_address()
    token_controller.clear_token()
    maze_controller.clear_custom_mazes()
    # scheduler.remove_job('1')
    return conn_details


"""
Routing for maze pages
"""
connection_page = Blueprint('connection_page', __name__)
instruction_page = Blueprint('instruction_page', __name__)


@connection_page.route('/connection', methods=['GET', 'POST'])
def connectionPage():
    token_controller.check_token()
    if request.method == 'POST':
        connect_to_car(request.form['ipInput'], request.form['portInput'])
        address = "http://" + conn.get_ip() + ":" + conn.get_port() + "/"
        testDat = {'ISN': 0, 'TOK': token_controller.get_token(), 'E': '#'}
        r = "200"
        if r == "200":
            r = token_controller.get_token()
            if token_controller.verify_token(r):
                print("Verified")
                # scheduler.add_job(dashboard_controller.foo, 'interval', seconds=1, id='1')
                stats_to_html = {
                    'Speed': 0,
                    'Closest': '-',
                    'Line': 'Yes',
                    'Distance': 0
                }
                return render_template('dashboard.html', render_stats=stats_to_html)
    return render_template('connection.html', address=disconnect())


@instruction_page.route('/instruction', methods=['GET', 'POST'])
def instructionPage():
    if request.method == 'POST':
        address = "http://" + conn.get_ip() + ":" + conn.get_port() + "/"
        testDat = {'ISN': 1, 'Direction': 'l', 'TOK': token_controller.get_token(), 'E': '#'}
        r = "200"
        if r == "200":
            r = token_controller.get_token()
            if token_controller.verify_token(r):
                print("Verified")
                return render_template('dashboard.html')
    return render_template('connection.html', address=disconnect())
