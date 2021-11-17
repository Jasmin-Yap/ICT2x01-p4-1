# import server
from flask import Blueprint, render_template

# from models.scoreboard import scoreboard.py


scoreboard_page = Blueprint('scoreboard_page', __name__)


@scoreboard_page.route('/scoreboard')
def display_scoreboard():
    return render_template('scoreboard.html')
