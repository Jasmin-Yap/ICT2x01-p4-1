from models.token import Token
import server
import secrets

class TokenController:
    def __init__(self):
        self.auth_token = Token()

    def generate_token(self):
        self.auth_token.set_token(secrets.token_urlsafe(16))
        # debugging
        server.logging.debug(self.auth_token.get_token())

    def verify_token(self, token_from_car):
        # server.logging.debug(self.auth_token.get_code())
        # server.logging.debug(code)
        return secrets.compare_digest(token_from_car, self.auth_token.get_token())
    
    def clear_token(self):
        del self.auth_token
        self.__init__()
