import logging

from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)


class LogRequestMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.info(f"Request received: {request.method} {request.path}")

        response = self.get_response(request)
        return response
