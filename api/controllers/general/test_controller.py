from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from sentence_transformers import SentenceTransformer, util

from api.ml_core.topic_modeling.lda_model import LDAModel
from api.repositories.general.security_aop import logging_and_security


class TestController(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        security=[{'Bearer': []}]
    )
    @logging_and_security
    @staticmethod
    def get(request, response):
        # lda_model = LDAModel()
        # model, corpus, id2word = lda_model.train(None)
        # topic_distribution = lda_model.analyze("Trump is a republican and i like pizza")
        # topic_distribution = sorted(topic_distribution, key=lambda x: x[1], reverse=True)
        #
        # model = SentenceTransformer('all-MiniLM-L6-v2')
        # texts = ["I love pizza.", "Is Trump a politician?", "FBI is an organization"]
        # embeddings = model.encode(texts, batch_size=16, convert_to_tensor=True)
        # similarities = util.cos_sim(embeddings, embeddings)

        response_data = {
            "message": "Hello world!",
            "status": "success"
        }
        return JsonResponse(response_data)
