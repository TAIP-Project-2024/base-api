from django.http import HttpResponse
from django.shortcuts import render

from api.models.domain.graph_drawing import GraphDrawing
from api.services.general.graph_drawing_service import GraphDrawingService
from api.services.general.graph_service import GraphService


def hello_world(request):
    """View to return the 'Hello, World!' HTML page."""
    return render(request, 'hello.html')

def display_graph(request):
    name = request.GET.get('name')
    html_file = GraphDrawingService().find_drawing_by_name(name)
    print(html_file)
    return HttpResponse(html_file, content_type='text/html')
