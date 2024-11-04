from django.urls import path, include

from api.controllers.general.test_controller import TestController

urlpatterns = [
    path("test/", TestController.as_view(), name="test"),
]
