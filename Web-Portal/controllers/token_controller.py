import secrets, logging
from models.token import Token
from flask import Blueprint, render_template

auth_token = Token()

"""
generating token using secrets
"""
def generate_token():
    auth_token.set_token(secrets.token_urlsafe(16))
    return auth_token.get_token()

"""
retrieving token
"""
def get_token():
    return auth_token.get_token()

"""
check if token exists
"""
def check_token():
    if auth_token.get_token() != None:
        return True
    else:
        generate_token()

"""
verify token with token from car
"""
def verify_token(token_from_car):
    return secrets.compare_digest(token_from_car, auth_token.get_token())

"""
clear the token
"""
def clear_token():
    auth_token.set_token(None)