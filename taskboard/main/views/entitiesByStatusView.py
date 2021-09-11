from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as st
from main.serializers import EntitySerializer
from main.functions import getUserGroup, getEntityByStatus
from rest_framework.permissions import IsAuthenticated

class EntitiesByStatusView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        status = kwargs.get('status')
        user_group = getUserGroup(self.request.user)
        if self.request.user.is_superuser:
            queryset = getEntityByStatus(status,user_group)
        else:
            queryset = getEntityByStatus(status,user_group,self.request.user)
        serializer = EntitySerializer(queryset,many=True)
        return Response(serializer.data, status=st.HTTP_200_OK)
                        

