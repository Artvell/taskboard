"""файл с классом EntitiesByStatusView"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status as st
from main.serializers import EntitySerializer
from main.functions import get_user_group,get_entity_by_status


class EntitiesByStatusView(APIView):
    """вьюха для получения списка Entity  с указанным статусом"""
    permission_classes = [IsAuthenticated]
    def get(self, request, **kwargs):
        """метод для обработки GET запроса"""
        status = kwargs.get('status')
        user_group = get_user_group(self.request.user)
        if self.request.user.is_superuser:
            queryset = get_entity_by_status(status,user_group)
        else:
            queryset = get_entity_by_status(status,user_group,self.request.user)
        serializer = EntitySerializer(queryset,many=True)
        return Response(serializer.data, status=st.HTTP_200_OK)
                        