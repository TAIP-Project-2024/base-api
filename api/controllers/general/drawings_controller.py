from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from api.models.domain.graph_drawing import GraphDrawing
from api.services.general.graph_drawing_service import GraphDrawingService


class DrawingsController(APIView):
    permission_classes = [AllowAny]


    @xframe_options_exempt
    def get(self, request):
        # Check the path to decide functionality
        print("here sss")
        if request.path.endswith("/drawings/"):
            return self.retrieve_drawing(request)
        elif request.path.endswith("/posts/"):
            return self.retrieve_comments_drawing(request)
        else:
            return HttpResponse("Invalid endpoint.", status=404)

    def retrieve_drawing(self, request):
        # Retrieve the 'name' query parameter
        name = request.query_params.get('name')  # Use .get() to avoid KeyError if 'name' is missing

        if not name:
            return HttpResponse("Name parameter is required.", status=400)

        # Call your service to find the drawing by name

        html_file = GraphDrawingService().find_drawing_by_name(name)
        # html = GraphDrawing(None, name).html_file
        # html_file = ""
        #
        # with open(html, "r") as file:
        #     html_file = file.read()
        # Log or debug
        # Return the HTML response
        return HttpResponse(html_file, content_type='text/html')

    def retrieve_comments_drawing(self, request):
        post_id = request.query_params.get('post_id')
        text = request.query_params.get('text') or 'post text'

        if not post_id:
            return HttpResponse("Post id is required.", status=400)
        html_file = GraphDrawingService().create_or_retrieve_comments_drawing(post_id, text)
        return HttpResponse(html_file, content_type='text/html')

