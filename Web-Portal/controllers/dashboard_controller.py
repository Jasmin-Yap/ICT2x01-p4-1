from flask import Blueprint, render_template


dashboard_page = Blueprint('dashboard_page', __name__)


@dashboard_page.route('/dashboard')
def display_dashboard():
    return render_template('dashboard.html')
