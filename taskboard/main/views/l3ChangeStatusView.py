from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from main.models import Entity
from main.permissions import L3Permission

class L3ChangeEntityStatusView(APIView):
    permission_classes = [L3Permission]
    def post(self, request, *args, **kwargs):
        entity_id = kwargs.get('id',"!")
        if entity_id == "!":
            return Response({"error":"ID is required"},status=status.HTTP_400_BAD_REQUEST)
        else:
            new_status = request.data.get("status","!")
            if new_status == "!" or (new_status!="5" and new_status!="6"):
                return Response({"error":"Wrong status"},status=status.HTTP_400_BAD_REQUEST)
            try:
                entity = Entity.objects.get(id=entity_id)
                entity.status = int(new_status)
                entity.save()
                return Response("Status changed",status=status.HTTP_200_OK)
            except Entity.DoesNotExist:
                return Response({"error":"Wrong ID: Entity not found"},status=status.HTTP_404_NOT_FOUND)
