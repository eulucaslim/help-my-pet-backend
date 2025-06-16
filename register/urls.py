from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register("register", RegisterClientViewset,
                basename="register")

router.register("login", LoginViewSet,
                basename="login")

router.register("all_users", AllUsersViewSet,
                basename="all_users")

urlpatterns = [
    path('', include(router.urls)),
]