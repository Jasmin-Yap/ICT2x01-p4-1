from models.token import Token
from flask import Blueprint, render_template
import server
import secrets

auth_token = Token()

def generate_token():
    auth_token.set_token(secrets.token_urlsafe(16))
    # debugging
    server.logging.debug(auth_token.get_token())

def verify_token(token_from_car):
    # server.logging.debug(self.auth_token.get_code())
    # server.logging.debug(code)
    return secrets.compare_digest(token_from_car, auth_token.get_token())

def clear_token():
    auth_token.set_token(None)

simple_page = Blueprint('simple_page', __name__)
@simple_page.route('/hello')
def hello():
    return render_template('maze.html')