from django.http import HttpResponse
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from api.services.general.graph_drawing_service import GraphDrawingService


class GraphsController(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        # Retrieve the 'name' query parameter
        name = request.query_params.get('name')  # Use .get() to avoid KeyError if 'name' is missing

        if not name:
            return HttpResponse("Name parameter is required.", status=400)

        # Call your service to find the drawing by name
        html_file = GraphDrawingService().find_drawing_by_name(name)

        # Log or debug
        print(html_file)

        # Return the HTML response
        return HttpResponse(html_file, content_type='text/html')