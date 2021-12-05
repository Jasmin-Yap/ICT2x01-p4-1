import sys, logging
from flask import Flask, render_template
from controllers import connection_controller, scoreboard_controller, dashboard_controller, token_controller, maze_controller

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

app = Flask(__name__)

app.register_blueprint(connection_controller.connection_page)
app.register_blueprint(connection_controller.instruction_page)

#generate auth token variable
token = token_controller


@app.route('/')
def connection():
    conn_details = connection_controller.get_address()
    return render_template('connection.html', address=conn_details)


# route to be moved to connection controller
@app.route('/dashboard')
def dash():
    # logging.debug(token.generate_token())
    token.generate_token()
    return render_template('dashboard.html')


app.register_blueprint(scoreboard_controller.scoreboard_page)
app.register_blueprint(dashboard_controller.dashboard_page)
app.register_blueprint(maze_controller.mazecreator_page)


@app.route('/')
def connection():
    return render_template('connection.html')


@app.route('/connection')
def end_session():
    token_controller.clear_token()
    maze_controller.clear_custom_mazes()
    return render_template('connection.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
