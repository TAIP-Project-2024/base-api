import os
import unittest
from unittest.mock import MagicMock, patch

import requests

from api.ml_core.topic_modeling.get_topic_name import GetTopicName


class MyTestCase(unittest.TestCase):
    def setUp(self):
        os.environ["GOOGLE_API_KEY"] = "test_api_key"
        self.get_topic_name = GetTopicName()

    @patch("requests.post")
    def test_get_content_success(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"content": "Test content"}
        mock_post.return_value = mock_response

        prompt = "Test prompt"
        result = self.get_topic_name.get_content(prompt)

        self.assertEqual(result, {"content": "Test content"})

        mock_post.assert_called_once_with(
            "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent",
            headers={"Content-Type": "application/json"},
            json={
                "contents": [{"parts": [{"text": prompt}]}]
            },
            params={"key": "test_api_key"},
            timeout=60
        )

    @patch("requests.post")
    def test_get_content_failure(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("500 Server Error")
        mock_post.return_value = mock_response

        prompt = "Test prompt"

        with self.assertRaises(RuntimeError):
            self.get_topic_name.get_content(prompt)

        mock_post.assert_called_once_with(
            "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent",
            headers={"Content-Type": "application/json"},
            json={
                "contents": [{"parts": [{"text": prompt}]}]
            },
            params={"key": "test_api_key"},
            timeout=60
        )

    def test_no_api_key(self):
        del os.environ["GOOGLE_API_KEY"]
        with self.assertRaises(ValueError):
            GetTopicName()

if __name__ == '__main__':
    unittest.main()
