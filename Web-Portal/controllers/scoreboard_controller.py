from flask import Blueprint, render_template
from models.scoreboard import Scoreboard
import pandas as pd
import os

scoreboard_page = Blueprint('scoreboard_page', __name__)
scoreboard = Scoreboard()


def read_csv():
    try:
        scoreboard.set_data('./static/data.csv')
        csv_data = scoreboard.get_data()
        return csv_data
    except FileNotFoundError:
        csv_data = pd.DataFrame({
            'Attempt': [0, 0, 0],
            'Score': [0, 0, 0]
        })
        path = './static/'
        csv_data.to_csv(os.path.join(path, r'data.csv'), index=False)
        scoreboard.set_data('./static/data.csv')
        csv_data = scoreboard.get_data()
        return csv_data


def sort_top_3(csv_data):
    top3 = csv_data.sort_values(csv_data.columns[1], ascending=False).head(3)
    scoreboard.set_attempt(top3)
    scoreboard.set_score(top3)


def check():



@scoreboard_page.route('/scoreboard')
def display_scoreboard():
    read_csv()
    sort_top_3(read_csv())
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
