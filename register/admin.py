from django.contrib import admin
from .models import Client, Veterinary

# Register your models here.

admin.site.register(Client)
admin.site.register(Veterinary)
