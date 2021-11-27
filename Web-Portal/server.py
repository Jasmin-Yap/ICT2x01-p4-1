import sys, logging
from flask import Flask, render_template
from controllers import token_controller

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

app = Flask(__name__)
app.register_blueprint(token_controller.simple_page)

#generate auth token variable
token = token_controller

@app.route('/')
def connection():
    return render_template('conn.html')

# route to be moved to connection controller
@app.route('/dashboard')
def dash():
    token.generate_token()
    return render_template('dashboard.html')

@app.route('/connection')
def end_session():
    token.clear_token()
    return render_template('conn.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 