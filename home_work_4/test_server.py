import unittest

from home_work_3.server import *
import time


class TestClient(unittest.TestCase):
    def test_message_response(self):
        correct_message = {
            ACTION: PRESENCE,
            TIME: time.time(),
            USER: {
                ACCOUNT_NAME: DEFAULT_ACCOUNT_NAME
            }
        }
        self.assertEqual(message_response(correct_message), {RESPONSE: 200})

    def test_message_response_incorrect(self):
        incorrect_message = {
        }
        self.assertEqual(message_response(incorrect_message), {RESPONSE: 400, ERROR: 'Incorrect request'})