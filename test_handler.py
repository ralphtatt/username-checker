import unittest
from unittest import mock

from handler import *

test_usernames_file = "Alice\nBob\nClaire\n\n"
test_domains_file = "https://web.com/$USERNAME\nhttps://sub.web.com/$USERNAME\n\n"

class TestUsernameChecker(unittest.TestCase):
    
    @mock.patch("handler.open", mock.mock_open(read_data=test_usernames_file))
    def test_get_usernames(self):
        # Test
        expected = ["alice", "bob", "claire"]

        # Act
        result = get_usernames()

        # Assert
        self.assertEqual(expected, result)


    @mock.patch("handler.open", mock.mock_open(read_data=test_domains_file))
    def test_get_domains(self):
        # Test
        expected = ["https://web.com/$username", "https://sub.web.com/$username"]

        # Act
        result = get_domains()

        # Assert
        self.assertEqual(expected, result)


    def test_generate_urls(self):
        # Test
        usernames = ["alice", "bob", "claire"]
        domains = ["https://web.com/$usercase", "https://sub.web.com/$usercase"]

        expected = [
            "https://web.com/alice", "https://sub.web.com/alice",
            "https://web.com/bob", "https://sub.web.com/bob",
            "https://web.com/claire", "https://sub.web.com/claire"
            ]

        # Act
        result = generate_urls(usernames, domains)

        # Assert
        self.assertEqual(expected, result)


    @mock.patch("handler.http.request", mock.MagicMock(status=200))
    def test_get_available_usernames(self):
        # Test
        urls = ["https://web.com/alice", "https://sub.web.com/alice"]

        # Act
        result = get_available_usernames(urls)

        # Assert
        self.assertEqual([], result)
