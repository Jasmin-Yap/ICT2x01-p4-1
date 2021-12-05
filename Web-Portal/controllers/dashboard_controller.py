from flask import Blueprint, render_template, Flask, request, jsonify
from controllers import token_controller, connection_controller
from models import blockly
import random

dashboard_page = Blueprint('dashboard_page', __name__)
block_arr = []


def get_stats(data):
    speed = random.randrange(3)
    distance = data + speed
    stats_to_html = {
        'Speed': speed,
        'Closest': 0,
        'Line': 'Yes',
        'Distance': distance
    }
    return stats_to_html


def get_instructions():
    instruction = block_arr
    return instruction


@dashboard_page.route('/dashboard', methods=['GET', 'POST'])
def blocklyPage():
    if request.method == 'POST':
        data = request.get_json()
        instructions = blockly.Blockly(data['instructions'])
        #obj.set_instructions(get_instructions(data['instructions']))
        #connection_controller.send_instruction(obj)
        result = {'processed': 'true'}
        return jsonify(result)
    token_controller.generate_token()
    return render_template('dashboard.html', data=get_instructions(), render_stats=get_stats(0))


@dashboard_page.route('/stats', methods=['POST'])
def display_dashboard():
    if request.method == "POST":
        data = request.get_json()
        results = get_stats(data["Distance"])
        return jsonify(results)
