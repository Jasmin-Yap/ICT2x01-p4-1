from flask import Blueprint, render_template, Flask
from controllers import token_controller
from apscheduler.schedulers.background import BackgroundScheduler


dashboard_page = Blueprint('dashboard_page', __name__)


def receive_stats():
    print('I am working...')


@dashboard_page.route('/dashboard')
def display_dashboard():
    scheduler = BackgroundScheduler()
    job = scheduler.add_job(receive_stats, 'interval', seconds=3)
    scheduler.start()
    token_controller.generate_token()
    return render_template('dashboard.html')
