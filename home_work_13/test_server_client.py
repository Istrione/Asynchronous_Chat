import time
import unittest
from sys import argv

import server, client
from home_work_13.jim import config


class TestSerever(unittest.TestCase):

    def setUp(self) -> None:
        self.response = 200
        self.content = "application/json"
        self.action = "presense"
        self.unix_time = time.time()
        self.account = "account_name"
        self.password = "password"

    def _get_link_server(self):
        parser = server.parser
        host_address = parser.parse_args(argv[1:])
        return host_address.addr, host_address.port

    def _get_link_client(self):
        parser = client.parser
        host_address = parser.parse_args(argv[1:])
        return host_address.addr, host_address.port

    def _get_msg_received_by_server_from_client(self):
        msg_to_serever = {
            "action": config.ACTION,
            "time": 1,
            "user": {
                "account": config.ACCOUNT,
                "password": config.CONTENT
            }
        }
        return msg_to_serever

    def _get_msg_resived_by_client_from_server(self):
        msg_to_client = {
            "response": config.STATUS_RESPONCE,
            "content": config.CONTENT
        }
        return msg_to_client

    def test_EqualMessageFromClient(self):
        msg = self._get_msg_resived_by_client_from_server()
        self.assertEqual(client.send_msg(), msg)

    def testEqualMessageFromServer(self):
        msg = self._get_msg_received_by_server_from_client()
        self.assertEqual(server.answer_msg(), msg)


    def test_EqualMessageSendFromClient(self):
        msg = self._get_msg_received_by_server_from_client()
        adr_client, port = self._get_link_server()
        self.assertEqual(server.resive_msg(server.data, server.addr), msg)
        self.assertEqual(server.resive_msg(server.data, server.addr), adr_client)

    def test_EqualMessageSendFromServer(self):
        msg = self._get_msg_received_by_server_from_client()
        self.assertEqual(client.answer_msg(client.data), msg)

    def test_get_notEmptyAddrPortServer(self):
        addr, port = self._get_link_server()
        self.assertTrue(bool(addr))
        self.assertTrue(bool(port))

    def test_get_notEmptyAddrPortClient(self):
        addr, port = self._get_link_client()
        self.assertTrue(bool(addr))
        self.assertTrue(bool(port))