from flask import Flask, render_template
from controllers import scoreboard_controller, dashboard_controller

app = Flask(__name__)
app.register_blueprint(scoreboard_controller.scoreboard_page)
app.register_blueprint(dashboard_controller.dashboard_page)


@app.route('/')
def connection():
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
