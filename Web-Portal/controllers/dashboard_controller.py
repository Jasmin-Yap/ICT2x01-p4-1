from flask import Blueprint, render_template, Flask, request, jsonify
from controllers import token_controller


dashboard_page = Blueprint('dashboard_page', __name__)
stuff_page = Blueprint('stuff_page', __name__)


def get_stats(i):
    i += 1
    stats_to_html = {
        'Speed': i,
        'Closest': '-',
        'Line': 'Yes',
        'Distance': i
    }
    return stats_to_html


@dashboard_page.route('/dashboard', methods=['POST', 'GET'])
def display_dashboard():
    if request.method == "POST":
        data = request.get_json()
        results = get_stats()
        return jsonify(results)

    token_controller.generate_token()
    return render_template('dashboard.html', render_stats=get_stats())
