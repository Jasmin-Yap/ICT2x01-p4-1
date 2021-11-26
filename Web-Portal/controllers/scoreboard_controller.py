from flask import Blueprint, render_template
from models.scoreboard import Scoreboard


scoreboard_page = Blueprint('scoreboard_page', __name__)

scoreboard = Scoreboard()

scoreboard.set_data('./static/data1.csv')
csv_data = scoreboard.get_data()


def sort_top_3():
    top3 = csv_data.sort_values(csv_data.columns[1], ascending=False).head(3)
    scoreboard.set_attempt(top3)
    scoreboard.set_score(top3)


@scoreboard_page.route('/scoreboard')
def display_scoreboard():
    sort_top_3()
    attempt = scoreboard.get_attempt()
    score = scoreboard.get_score()
    scoreboard_data = {
        'date': scoreboard.get_date(),
        'rank1attempt': attempt[0],
        'rank2attempt': attempt[1],
        'rank3attempt': attempt[2],
        'rank1score': score[0],
        'rank2score': score[1],
        'rank3score': score[2],
    }
    return render_template('scoreboard.html', scoreboard_py=scoreboard_data)
