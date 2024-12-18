import json
from unittest.mock import patch

from django.test import TestCase, RequestFactory

from api.controllers.general.test_controller import TestController


class TestTestController(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.controller = TestController.as_view()

    def test_get_success(self):
        # Create a request for the GET endpoint
        request = self.factory.get("/test/")
        response = self.controller(request)

        # Verify the response status code and content
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["message"], "Hello world!")
        self.assertEqual(response_data["status"], "success")
