from django.http import JsonResponse
from django.views import View
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from api.repositories.general.security_aop import logging_and_security


class TestController(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        security=[{'Bearer': []}]
    )
    @logging_and_security
    def get(request, response):
        response_data = {
            "message": "Hello world!",
            "status": "success"
        }
        return JsonResponse(response_data)
