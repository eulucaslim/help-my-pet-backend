from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Client
from .serializers import ClientSerializer, LoginSerializer
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

class LoginViewSet(viewsets.ViewSet):
    serializer_class = LoginSerializer

    def create(self, request):
        if request.method == "POST":
            try:
                response = self.verify_password(request.data)
                return Response({
                    "status": status.HTTP_200_OK,
                    "message": f"{response}"})
            except Exception as e:
                return Response({
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": str(e)}
                )

    def verify_password(self, data: dict) -> str:
        try:
            client = authenticate(username=data['username'], password=data['password'])
            return "Login Realizado com Sucesso!"
        except Exception:
            raise ("Usuário ou Senha estão incorretos!")

class AllUsersViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
