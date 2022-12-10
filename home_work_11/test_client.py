import unittest
from home_work_11.client import *
import home_work_11.server
import time
import threading
import re
import ast

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch


class TestClient(unittest.TestCase):
    def test_create_message(self):
        correct_message = {
            ACTION: PRESENCE,
            TIME: time.time(),
            USER: {
                ACCOUNT_NAME: DEFAULT_ACCOUNT_NAME
            }
        }
        message_created = create_message()
        self.assertEqual(type(message_created), type(correct_message))
        self.assertEqual(message_created[ACTION], correct_message[ACTION])
        self.assertAlmostEqual(message_created[TIME], correct_message[TIME], 3)
        self.assertEqual(message_created[USER], correct_message[USER])

    def test_create_message_with_account_name(self):
        self.assertEqual(create_message('Kostia')[USER][ACCOUNT_NAME], 'Kostia')

    def test_create_message_exception_too_long(self):
        with self.assertRaises(UsernameTooLongError):
            create_message('thisnameisreallyreallytoolong')

    def test_create_message_exception_wrong_type(self):
        with self.assertRaises(TypeError):
            create_message(1)

    def test_translate_message_exception_not_dict(self):
        with self.assertRaises(TypeError):
            translate_message('')

    def test_translate_message_exception_no_response(self):
        with self.assertRaises(MandatoryKeyError):
            translate_message({})

    def test_translate_message_exception_response_code_error(self):
        with self.assertRaises(ResponseCodeLenError):
            translate_message({RESPONSE: 1000})

    def test_translate_message_exception_response_code_not_known(self):
        with self.assertRaises(ResponseCodeError):
            translate_message({RESPONSE: 404})

    def test_translate_message(self):
        self.assertEqual(translate_message({RESPONSE: OK}), {RESPONSE: OK})

    def test_communication(self):
        th = threading.Thread(target=home_work_11.server.main)
        th.daemon = True
        th.start()
        correct_message = [
            {
                ACTION: PRESENCE,
                TIME: time.time(),
                USER: {
                    ACCOUNT_NAME: DEFAULT_ACCOUNT_NAME
                }
            },
            {
                RESPONSE: OK
            }
        ]
        with unittest.mock.patch('builtins.print') as mocked_print:
            main()
        for idx, callstr in enumerate(mocked_print.mock_calls):
            message_created = ast.literal_eval(
                re.search(r'call\((.*?)\)', str(callstr)).group(1)
            )
            for key, value in correct_message[idx].items():
                if key != TIME:
                    self.assertEqual(message_created[key], value)
                else:
                    self.assertAlmostEqual(message_created[key], value, 1)


if __name__ == "__main__":
    unittest.main()