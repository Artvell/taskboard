from authentification.models import User, TmpPass
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from authentification.functions import Encoder, SendMail

class ActivateUserView(APIView):
    def get(self, request, user):
        decoded_username = Encoder(user).decode()
        user = User.objects.get(username=decoded_username)
        if user:
            if not user.is_active:
                tmp_user = TmpPass.objects.get(username=decoded_username)
                user.is_active = True
                user.save()
                resp = {"status":"Аккаунт активирован"}
                text = f"Логин: {user.username}\nПароль: {tmp_user.password}"
                SendMail(text,[user.email]).send()
                tmp_user.delete()
                return Response(resp,status=status.HTTP_200_OK)
            else:
                return Response({"error":"Этот аккаунт уже активен"},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error":"Incorrect link"},status=status.HTTP_400_BAD_REQUEST)