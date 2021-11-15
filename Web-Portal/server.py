import sys
from flask import Flask, render_template
from controllers.token_controller import TokenController
import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

app = Flask(__name__)

#generate auth token variable
token = TokenController()

@app.route('/')
def connection():
    return render_template('conn.html')

@app.route('/dashboard')
def dash():
    token.generate_token()
    logging.debug(token.verify_token(token.auth_token.get_code()))
    logging.debug(token.verify_token("N2u-9nAzeR6brtz-MNts7g"))
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 