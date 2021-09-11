from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from main.models import Entity

class OwnEntitiesView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Entity.objects.filter()
