from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from authentication.serializers import UserSerializer


class UserRegistration(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            serializer.save()
            return Response({'message': 'Registration successful'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        data = {
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'is_superuser': user.is_superuser,
        }
        return Response(data)

    def put(self, request):
        user = request.user
        new_data = request.data

        allowed_fields = ['email', 'first_name', 'last_name']

        for field in allowed_fields:
            if field in new_data:
                setattr(user, field, new_data[field])

        new_password = new_data.get('password')
        if new_password:
            user.password = make_password(new_password)

        user.save()

        return Response({'message': 'Profile has been updated successfully'})
