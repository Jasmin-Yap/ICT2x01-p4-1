from flask import Blueprint, render_template, redirect, request, jsonify
from models.scoreboard import Scoreboard
from controllers import token_controller
import pandas as pd


scoreboard_page = Blueprint('scoreboard_page', __name__)


def get_csv(path, scoreboard_object):
    while True:
        try:
            scoreboard_object.set_data(path)
            return scoreboard_object.get_data()
        except FileNotFoundError:
            csv_data = pd.DataFrame({
                'Name': ['-', '-', '-', '-', '-'],
                'Date': ['-', '-', '-', '-', '-'],
                'Score': ['-', '-', '-', '-', '-']
            })
            csv_data.to_csv(path, index=False)
            scoreboard_object.set_data(path)
            return scoreboard_object.get_data()


def sort_top_5(csv_data):
    length = len(csv_data)
    csv_data_descending_order = csv_data.sort_values(csv_data.columns[2], ascending=True).head(length)
    csv_data_descending_order = csv_data_descending_order.drop_duplicates(subset='Name' and 'Score')
    top5 = csv_data_descending_order.sort_values(csv_data_descending_order.columns[2], ascending=True).head(5)
    return top5


def validate_data(data, scoreboard_object):
    name_array = []
    date_array = []
    score_array = []
    for i in range(5 - len(data)):
        name_array.append('-')
        date_array.append('-')
        score_array.append('-')
    add_data = pd.DataFrame({
        'Name': name_array,
        'Date': date_array,
        'Score': score_array
    })
    data = data.append(add_data, ignore_index=True)
    scoreboard_object.set_name(data)
    scoreboard_object.set_date(data)
    scoreboard_object.set_score(data)
    return data


def scoreboard_data(scoreboard_maze):
    name = scoreboard_maze.get_name()
    date = scoreboard_maze.get_date()
    score = scoreboard_maze.get_score()
    data = {
        'rank1name': name[0],
        'rank2name': name[1],
        'rank3name': name[2],
        'rank4name': name[3],
        'rank5name': name[4],
        'rank1date': date[0],
        'rank2date': date[1],
        'rank3date': date[2],
        'rank4date': date[3],
        'rank5date': date[4],
        'rank1score': score[0],
        'rank2score': score[1],
        'rank3score': score[2],
        'rank4score': score[3],
        'rank5score': score[4],
    }
    return data


@scoreboard_page.route('/scoreboard')
def display_scoreboard():
    if not token_controller.check_token():
        return redirect('/')
    scoreboards = [Scoreboard(), Scoreboard(), Scoreboard()]
    paths = ['./static/data/maze_1.csv', './static/data/maze_2.csv', './static/data/maze_3.csv']
    scoreboard_data_to_html = []
    for scoreboard_object, path_to_data in zip(scoreboards, paths):
        validate_data(sort_top_5(get_csv(path_to_data, scoreboard_object)), scoreboard_object)
        scoreboard_data_to_html.append(scoreboard_data(scoreboard_object))

    return render_template('scoreboard.html', scoreboard_py=scoreboard_data_to_html)


@scoreboard_page.route('/updateScoreboard', methods=['POST'])
def update_scoreboard():
    if request.method == 'POST':
        data = request.get_json()
        mazeID = data['mazeID']
        date = data['date']
        score = data['score']

        if mazeID == "Maze 1":
            path = './static/data/maze_1.csv'
        elif mazeID == "Maze 2":
            path = './static/data/maze_2.csv'
        elif mazeID == "Maze 3":
            path = './static/data/maze_3.csv'
        else:
            result = {'processed':False}
            return jsonify(result)
        
        f = open(path, "a")
        f.write("\n" + token_controller.get_studentName() + "," + date + "," + str(score))
        f.close()
        result = {'processed': True}
        return jsonify(result)
