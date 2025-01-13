from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from requests import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from api.repositories.general.favourite_graphs_repository import FavouriteGraphsRepository


class FavouritesController(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        user_id = request.user.id
        favourites = FavouriteGraphsRepository().get_by_user_id(user_id)
        serialized = [{'graph_id': f.get('graph_id')} for f in favourites]
        return JsonResponse({'favourites': serialized})

    def post(self, request):
        user_id = request.user.id
        graph_id = request.data.get('graph_id')
        FavouriteGraphsRepository().save(favourite_graph={'graph_id': graph_id, 'user_id': user_id})
        return JsonResponse({'status': 'Graph saved to favourites'})

    def delete(self, request):
        user_id = request.user.id
        graph_id = request.data.get('graph_id')
        FavouriteGraphsRepository().delete(favourite_graph={'graph_id': graph_id, 'user_id': user_id})
        return JsonResponse({'status': 'Graph removed from favourites'})
