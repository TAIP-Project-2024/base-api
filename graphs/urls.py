from django.urls import path

from graphs import views

urlpatterns = [
    path('hello/', views.hello_world, name = 'hello_world'),
    path('drawing/', views.display_graph),

]
