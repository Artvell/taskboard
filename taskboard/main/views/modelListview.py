from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from main.models import Passport,Category,Keywords,Entity
from main.serializers import ModelsListSerializer

class ModelListView(APIView):
    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            model = kwargs.get('model')
            entity = kwargs.get("entity")
            data=""
            if model == "categories":
                data = Entity.objects.get(id=entity).category.all()
            elif model == "keywords":
                data = Entity.objects.get(id=entity).keywords.all()
            elif model == "passports":
                data = Passport.objects.filter(entity__id=entity)
            serializer = ModelsListSerializer(data=data)
            if serializer.is_valid():
                return Response(serializer.data)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
