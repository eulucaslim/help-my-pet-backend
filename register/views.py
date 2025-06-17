from django.contrib.auth.hashers import make_password
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Client
from .serializers import ClientSerializer
from datetime import datetime

# Create your views here.
class RegisterClientViewset(viewsets.ViewSet):
    serializer_class = ClientSerializer

    def create(self, request):
        if request.method == "POST":
            try:
                params = self.filter_values(request.data)
                Client.objects.create(**params)
                return Response({
                    "status": status.HTTP_201_CREATED,
                    "message": "Usuário Criado com Sucesso!"})
            except Exception as e:
                return Response({
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": str(e)}
                )
        
    def filter_values(self, request_data: dict) -> dict:
        params = dict()
        for key, value in request_data.items():
            if value != None:
                params[key] = value

        params['password'] = make_password(params['password'])
        params['date_of_birth'] = datetime.strptime(params["date_of_birth"],'%Y-%m-%d')
        if params.get('csrfmiddlewaretoken'):
            del params['csrfmiddlewaretoken']
        return params


class AllUsersViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
