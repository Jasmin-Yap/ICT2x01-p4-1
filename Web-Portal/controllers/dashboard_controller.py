from flask import Blueprint, render_template, Flask
from controllers import token_controller

dashboard_page = Blueprint('dashboard_page', __name__)


@dashboard_page.route('/dashboard')
def display_dashboard():
    stats_to_html = {
        'Speed': 10,
        'Closest': 5,
        'Line': 'Yes',
        'Distance': 100
    }
    token_controller.generate_token()
    return render_template('dashboard.html', render_stats=stats_to_html)
