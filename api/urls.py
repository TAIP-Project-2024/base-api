from django.urls import path

from api.controllers.general.graphs_controller import GraphsController
from api.controllers.general.test_controller import TestController

urlpatterns = [
    path("test/", TestController.as_view(), name="test"),
    path("graphs/", GraphsController.as_view(), name="graphs"),
]
