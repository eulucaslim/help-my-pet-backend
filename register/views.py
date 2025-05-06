from django.contrib.auth.hashers import make_password
from rest_framework import viewsets
from .models import Client

# Create your views here.
class RegisterClientViewset(viewsets.ViewSet):
    def create(self, request):
        if request.method == "POST":
            params = self.filter_values(request.data)
            client = Client.objects.filter(**params).first()
            
            if not client:
                client = Client.objects.create(**params)
        
    def filter_values(self, request_data: dict) -> dict:
        for key, value in request_data.items():
            params = dict()
            if value != None:
                params[key] = value
        return params