# myapp/middleware.py

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from rest_framework_simplejwt.authentication import JWTAuthentication


class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Attempt to authenticate the user using JWT
        jwt_auth = JWTAuthentication()
        try:
            # Authenticate the user
            user, _ = jwt_auth.authenticate(request)
            request.user = user  # Set the user to request object
        except Exception as e:
            request.user = None  # No user authenticated

        response = self.get_response(request)
        return response
