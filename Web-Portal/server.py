import sys, logging, gc, copy
from flask import Flask, render_template
from controllers import token_controller

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

app = Flask(__name__)

#generate auth token variable
token = token_controller.TokenController()

@app.route('/')
def connection():
    return render_template('conn.html')

@app.route('/dashboard')
def dash():
    token.generate_token()
    logging.debug("verify token (True): {0}".format(token.verify_token(token.auth_token.get_token())))
    logging.debug("verify token (False): {0}".format(token.verify_token("N2u-9nAzeR6brtz-MNts7g")))
    return render_template('dashboard.html')

@app.route('/connection')
def end_session():
    token.clear_token()
    logging.debug("token after deletion: {0}".format(token.auth_token.get_token()))
    return render_template('conn.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 