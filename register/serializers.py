from rest_framework import serializers
from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True, required=True)
    full_name = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)
    profile_picture = serializers.ImageField(required=False)
    date_of_birth = serializers.DateField()

    class Meta:
        model = Client
        fields = ['username', 'full_name', 'email', 'password', 'profile_picture', 'date_of_birth']