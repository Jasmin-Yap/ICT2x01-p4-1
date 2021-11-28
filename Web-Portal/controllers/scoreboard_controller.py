from flask import Blueprint, render_template
from models.scoreboard import Scoreboard
import pandas as pd
import os
import logging


scoreboard_page = Blueprint('scoreboard_page', __name__)
scoreboard = Scoreboard()

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


def get_csv(path):
    while True:
        try:
            scoreboard.set_data(path)
            logging.info('Found data file!')
            return scoreboard.get_data()
        except FileNotFoundError:
            logging.warning('Data file not found! Creating empty data file!')
            csv_data = pd.DataFrame({
                'Attempt': [0, 0, 0],
                'Score': [0, 0, 0]
            })
            csv_data.to_csv(path, index=False)
            logging.warning('Created empty data file')
            scoreboard.set_data(path)
            logging.warning('Reading newly created data file!')
            csv_data = scoreboard.get_data()
            return csv_data


def sort_top_3(csv_data):
    top3 = csv_data.sort_values(csv_data.columns[1], ascending=False).head(3)
    scoreboard.set_attempt(top3)
    scoreboard.set_score(top3)


def validate_data(data, path):
    logging.info('Starting validation!')
    if len(data) == 0:
        logging.info('0 row detected! Appending required data')
        add_data = pd.DataFrame({
            'Attempt': [0, 0, 0],
            'Score': [0, 0, 0]
        })
        new_data = data.append(add_data, ignore_index=True)
        new_data.to_csv(path, index=False)
        logging.info('Append success!')
        logging.info('Validation completed!')
        return new_data
    elif len(data) == 1:
        logging.info('1 row detected! Appending required data')
        add_data = pd.DataFrame({
            'Attempt': [0, 0],
            'Score': [0, 0]
        })
        new_data = data.append(add_data, ignore_index=True)
        new_data.to_csv(path, index=False)
        logging.info('Append success!')
        logging.info('Validation completed!')
        return new_data
    if len(data) == 2:
        logging.info('2 row detected! Appending required data')
        add_data = pd.DataFrame({
            'Attempt': [0],
            'Score': [0]
        })
        new_data = data.append(add_data, ignore_index=True)
        new_data.to_csv(path, index=False)
        logging.info('Append success!')
        logging.info('Validation completed!')
        return new_data
    else:
        logging.info('No missing data!')
        logging.info('Validation completed!')
        return data


def scoreboard_test(path_no_file, path_no_data, path_1_data, path_2_data, path_multiple_data):
    logging.info('')
    logging.info('Scoreboard test initiated!')

    logging.info('')
    logging.info('Test case: No data file - INITIATED!')
    validate_data(get_csv(path_no_file), path_no_file)
    logging.info('Removing dummy file!')
    os.remove(path_no_file)
    logging.info('Dummy file removed!')
    logging.info('Test case: No data file - COMPLETED!')

    logging.info('')
    logging.info('Test case: Empty data file - INITIATED!')
    logging.info('Using dummy file!')
    validate_data(get_csv(path_no_data), path_no_data)
    logging.info('Resetting dummy file!')
    csv_data = pd.read_csv(path_no_data)
    csv_data = csv_data.drop([0, 1, 2])
    csv_data.to_csv(path_no_data, index=False)
    logging.info('Dummy file reset!')
    logging.info('Test case: Empty data file - COMPLETED!')

    logging.info('')
    logging.info('Test case: 1 data file - INITIATED!')
    logging.info('Using dummy file!')
    validate_data(get_csv(path_1_data), path_1_data)
    logging.info('Resetting dummy file!')
    csv_data = pd.read_csv(path_1_data)
    csv_data = csv_data.drop([1, 2])
    csv_data.to_csv(path_1_data, index=False)
    logging.info('Dummy file reset!')
    logging.info('Test case: 1 data file - COMPLETED!')

    logging.info('')
    logging.info('Test case: 2 data file - INITIATED!')
    logging.info('Using dummy file!')
    validate_data(get_csv(path_2_data), path_2_data)
    logging.info('Resetting dummy file!')
    csv_data = pd.read_csv(path_2_data)
    csv_data = csv_data.drop([2])
    csv_data.to_csv(path_2_data, index=False)
    logging.info('Dummy file reset!')
    logging.info('Test case: 2 data file - COMPLETED!')

    logging.info('')
    logging.info('Test case: Multiple data file - INITIATED!')
    logging.info('Using dummy file!')
    validate_data(get_csv(path_multiple_data), path_multiple_data)
    logging.info('Test case: Multiple data file - COMPLETED!')

    logging.info('')
    logging.info('Scoreboard test completed!')
    logging.info('')
    return None


@scoreboard_page.route('/scoreboard')
def display_scoreboard():
    path = './static/data/data.csv'
    path_no_file = './static/data/dummy.csv'
    path_no_data = './static/data/data0.csv'
    path_1_data = './static/data/data1.csv'
    path_2_data = './static/data/data2.csv'
    path_multiple_data = './static/data/data999.csv'

    scoreboard_test(path_no_file, path_no_data, path_1_data, path_2_data, path_multiple_data)
    logging.info('Running scoreboard!')
    sort_top_3(validate_data(get_csv(path), path))
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
