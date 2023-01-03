from rest_framework import serializers
from django.contrib.auth.models import User
from .models import TranscationsData




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','first_name']


class TransSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranscationsData
        fields = '__all__'
