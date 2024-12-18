from unittest import mock

from django.test import TestCase
from django.urls import reverse


class TestDrawingsController(TestCase):

    @mock.patch("api.services.general.graph_drawing_service.GraphDrawingService.find_drawing_by_name")
    def test_retrieve_drawing_valid_name(self, mock_find_drawing_by_name):
        # Mock the service response
        mock_find_drawing_by_name.return_value = "<html><body>Mock Drawing</body></html>"

        # Send a GET request to the drawings endpoint
        response = self.client.get(reverse("drawings"), {"name": "test_drawing"})

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "text/html")
        self.assertIn("Mock Drawing", response.content.decode())
        mock_find_drawing_by_name.assert_called_once_with("test_drawing")

    def test_retrieve_drawing_missing_name(self):
        # Send a GET request without the 'name' parameter
        response = self.client.get(reverse("drawings"))

        # Assertions
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content.decode(), "Name parameter is required.")

    @mock.patch("api.services.general.graph_drawing_service.GraphDrawingService.create_or_retrieve_comments_drawing")
    def test_retrieve_comments_drawing_valid_post_id(self, mock_create_or_retrieve_comments_drawing):
        # Mock the service response
        mock_create_or_retrieve_comments_drawing.return_value = "<html><body>Mock Comments Drawing</body></html>"

        # Send a GET request to the posts endpoint
        response = self.client.get(reverse("posts"), {"post_id": "123", "text": "Mock post text"})

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "text/html")
        self.assertIn("Mock Comments Drawing", response.content.decode())
        mock_create_or_retrieve_comments_drawing.assert_called_once_with("123", "Mock post text")

    def test_retrieve_comments_drawing_missing_post_id(self):
        # Send a GET request without the 'post_id' parameter
        response = self.client.get(reverse("posts"), {"text": "Some text"})

        # Assertions
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content.decode(), "Post id is required.")

    def test_invalid_endpoint(self):
        # Send a GET request to an invalid endpoint
        response = self.client.get("/invalid_endpoint/")

        # Assertions
        self.assertEqual(response.status_code, 404)
        self.assertIn("Not Found", response.content.decode())

    @mock.patch("api.services.general.graph_drawing_service.GraphDrawingService.find_drawing_by_name")
    def test_xframe_options_exempt(self, mock_find_drawing_by_name):
        # Mock the service response
        mock_find_drawing_by_name.return_value = "<html><body>Mock Drawing</body></html>"

        # Send a GET request to the drawings endpoint
        response = self.client.get(reverse("drawings"), {"name": "test_drawing"})

        # Assertions
        self.assertNotIn("X-Frame-Options", response.headers)
        self.assertEqual(response.status_code, 200)