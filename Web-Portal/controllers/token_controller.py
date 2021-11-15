from models.token import Token
import server
import secrets

class TokenController:
    def __init__(self):
        self.auth_token = Token()

    def generate_token(self):
        self.auth_token.set_code(secrets.token_urlsafe(16))
        # debugging
        server.logging.debug(self.auth_token.get_code())

    def verify_token(self, code):
        # server.logging.debug(self.auth_token.get_code())
        # server.logging.debug(code)
        return secrets.compare_digest(code, self.auth_token.get_code())
