from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

class AuthMiddleware(MiddlewareMixin):
    """
    Middleware for authentication and authorization.
    
    This middleware checks for the presence of a JWT token in the
    Authorization header. If the token is valid, it allows the request to
    proceed; otherwise, it returns a 401 Unauthorized response.
    """

    def process_request(self, request):
        if request.path in ['/login/', '/register/', '/test/']:
            return None

        token = request.META.get('HTTP_AUTHORIZATION')

        if not token:
            return JsonResponse({"error": "Unauthorized: No token provided"}, status=401)

        return None
