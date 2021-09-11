from authentification.models import User
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from authentification.serializers import UserSerializer
from rest_framework.parsers import JSONParser
from random import choice
from string import ascii_uppercase,ascii_lowercase , digits
from authentification.functions import Encoder,SendMail

class CreateNewUserView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser]
    def post(self, request, format=None):
        email = request.data.get("email","!")
        role = request.data.get("status","!")
        if (email != "!" and role != "!"):
            username = "{}_{}".format(role,''.join(choice(ascii_uppercase + ascii_lowercase + digits) for _ in range(12)))
            password = ''.join(choice(ascii_uppercase + ascii_lowercase + digits) for _ in range(15))
            serializer = UserSerializer(
                data={
                    "username":username,
                    "password":password,
                    "email":email,
                    "is_active":False
                    }
                )
            if serializer.is_valid():
                serializer.save()
                encoded_username = Encoder(username).encode()
                scheme = request.is_secure() and "https" or "http"
                host = f'{scheme}://{request.get_host()}/'
                text = f'Перейдите по ссылке: {host}api/auth/activateUser/{encoded_username}/ для активации вашего аккаунта'
                SendMail(text,[email]).send()
                return Response(status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error":"email & status are required"}, status=status.HTTP_400_BAD_REQUEST)