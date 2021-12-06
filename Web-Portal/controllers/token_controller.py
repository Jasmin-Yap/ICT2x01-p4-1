import secrets
from models.token import Token
auth_token = Token()

"""
generating token using secrets
"""
def generate_token(studentName):
    auth_token.set_token(secrets.token_urlsafe(16))
    auth_token.set_studentName(studentName)
    return auth_token.get_token()

"""
retrieving token
"""
def get_token():
    return auth_token.get_token()

"""
retrieving student name
"""
def get_studentName():
    return auth_token.get_studentName()

"""
check if token exists
"""
def check_token():
    if auth_token.get_token() != None:
        return True
    else:
        return False

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
    auth_token.set_studentName(None)