from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Client
from .serializers import ClientSerializer
from datetime import datetime, date


class RegisterClientViewset(viewsets.ViewSet):
    serializer_class = ClientSerializer
    permission_classes = [AllowAny]
    authentication_classes = [JWTAuthentication]

    def create(self, request):
        if request.method == "POST":
            try:
                params = self.filter_values(request.data)
                if params:
                    client = Client.objects.filter(username=params['username']).first()
                    if not client:
                        Client.objects.create(**params)
                        return Response({
                            "status": status.HTTP_201_CREATED,
                            "message": "Usuário Criado com Sucesso!"})
                    else:
                        raise Exception("Já existe um usuário com este username!")
                    
            except Exception as e:
                return Response({
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": str(e)}
                )
        
    def filter_values(self, request_data: dict) -> dict:
        params = dict()
        for key, value in request_data.items():
            if key != "csrfmiddlewaretoken":
                if value != None:
                    params[key] = value

        params['password'] = make_password(params['password'])
        params['date_of_birth'] = datetime.strptime(params["date_of_birth"],'%Y-%m-%d')
        
        self.verify_birthday(params['date_of_birth'])

        return params

    def verify_birthday(self, birthday_date: date) -> bool | Exception:
        date_today = date.today()
        age_user = date_today.year - birthday_date.year - (
            (date_today.month, date_today.day ) < (birthday_date.month, birthday_date.day)
        )
        if age_user >= 18:
            return True
        else:
            raise Exception("Você não possui a idade mínima de 18 anos para criar uma conta")


class AllUsersViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [AllowAny]
    authentication_classes = [JWTAuthentication]
