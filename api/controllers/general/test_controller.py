from django.http import JsonResponse
from django.views import View


class TestController(View):
    def get(request, response):
        response_data = {
            "message": "Hello world!",
            "status": "success"
        }
        return JsonResponse(response_data)
