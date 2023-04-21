from rest_framework import serializers
from .models import Table1, Table2

from django.contrib.auth.models import User


class Table1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Table1
        fields = '__all__'

class Table2Serializer(serializers.ModelSerializer):
    table1 = Table1Serializer(read_only=True)
    
    class Meta:
        model = Table2
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')