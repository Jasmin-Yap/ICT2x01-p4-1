from flask import Blueprint, render_template
from controllers import token_controller


dashboard_page = Blueprint('dashboard_page', __name__)


@dashboard_page.route('/dashboard')
def display_dashboard():
    token_controller.generate_token()
    return render_template('dashboard.html')
