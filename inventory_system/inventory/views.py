from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Profile


def index(request):
    return render(request, 'index.html')

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    if request.method == 'POST':
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            phone_number = request.data.get('phone_number')
            if not username or not password or not phone_number:
                return Response({"message": "username ,password and phone_number is mandatory for user creation"}, status=status.HTTP_201_CREATED)
            user = User.objects.create_user(username=username, password=password)
            profile=Profile.objects.create(user=user,phone_number=phone_number)
            profile.save()
            return Response({"message": "User created successfully."}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    return Response({"error": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)
