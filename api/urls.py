from django.urls import path

from api.controllers.general.drawings_controller import DrawingsController
from api.controllers.general.favourites_controller import FavouritesController
from api.controllers.general.test_controller import TestController

urlpatterns = [
    path("test/", TestController.as_view(), name="test"),
    path("drawings/", DrawingsController.as_view(), name="drawings"),
    path("drawings/posts/", DrawingsController.as_view(), name="posts"),
    path("favourites", FavouritesController.as_view(), name="favourites"),
]
