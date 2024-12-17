from django.http import JsonResponse
from django.views import View
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from api.repositories.general.security_aop import logging_and_security
from api.ml_core.topic_modeling.lda_model import LDAModel
from sentence_transformers import SentenceTransformer, util

class TestController(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        security=[{'Bearer': []}]
    )
    @logging_and_security
    def get(request, response):
        lda_model = LDAModel()
        model, corpus, id2word = lda_model.train(None)
        topic_distribution = lda_model.analyze("Trump is a republican and i like pizza")
        topic_distribution = sorted(topic_distribution, key=lambda x: x[1], reverse=True)

        topics = ["Political Commentary/Games", "Gaming Technology and Services", "Mobile Phone Filmmaking", "Software and Technology", "Cybersecurity"]

        model = SentenceTransformer('all-MiniLM-L6-v2')

        # Example batch of texts
        texts = ["I love pizza.", "Is Trump a politician?", "FBI is an organization"]
        embeddings = model.encode(texts, batch_size=16, convert_to_tensor=True)

        # Compute similarities
        similarities = util.cos_sim(embeddings, embeddings)
        print(similarities)

        response_data = {
            "message": "Hello world!",
            "status": "success"
        }
        return JsonResponse(response_data)
