from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Table1, Table2
from .serializer import Table2Serializer,UserSerializer

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response



class Table2ListCreateView(generics.ListCreateAPIView):
    queryset = Table2.objects.all()
    serializer_class = Table2Serializer

class Table2DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Table2.objects.all()
    serializer_class = Table2Serializer



@api_view(['POST'])
def obtain_auth_token(request):
    """
    API view to obtain an authentication token for a user
    """
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request=request, username=username, password=password)
    if user is None:
        return Response({'error': 'Invalid credentials'})

    token, _ = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(user)

    return Response({
        'token': token.key,
        'userid': user.id,
        'username': user.username,
    })