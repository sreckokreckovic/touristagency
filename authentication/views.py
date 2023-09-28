from datetime import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView
from authentication.serializers import UserSerializer
import jwt, datetime


class UserRegistration(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            serializer.save()
            return Response({'message': 'Registration successful'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogin(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('User not found!')
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
        'id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=60),
        'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret' , algorithm = 'HS256')
        return Response({'jwt': token})



class UserLogout(APIView):
    def post(self,request):
        logout(request)
        return Response(
            status= status.HTTP_200_OK
        )

