from flask import Blueprint, render_template, jsonify, request
from controllers import token_controller, connection_controller
from models import blockly

dashboard_page = Blueprint('dashboard_page', __name__)
block_arr = []

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
    return render_template('dashboard.html', data=get_instructions())

