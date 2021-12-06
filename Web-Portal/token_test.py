import unittest
from controllers.token_controller import *
token = ''

class TestToken(unittest.TestCase):
    """
    Methods tested:
    token controller - generate_token(), get_token(), get_studentName(), check_token()
    token model - __init__(), get_token(), set_token(), get_studentName(), set_studentName()
    """
    def test_generating_token(self):
        global token
        self.assertRegex(generate_token("tester"), r'[a-zA-Z0-9_-]{16}')
        token = get_token()
        self.assertIsNotNone(get_token())
        self.assertEqual(get_token(), token)
        self.assertIsNotNone(get_studentName())
        self.assertEqual(get_studentName(), "tester")
        self.assertTrue(check_token())
    
    """
    Methods tested:
    token controller - verify_token()
    token model - get_token()
    """
    def test_verifying_token(self):
        global token
        self.assertFalse(verify_token("random token"))
        self.assertTrue(verify_token(token))
    
    """
    Methods tested:
    token controller - clear_token(), check_token(), get_token(), get_studentName()
    token model - get_token(), set_token(), get_studentName(), set_studentName()
    """
    def test_clearing_token(self):
        clear_token()
        self.assertFalse(check_token())
        self.assertIsNone(get_token())
        self.assertIsNone(get_studentName())
    
