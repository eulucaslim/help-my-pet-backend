from django.db import models

class Client(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=80, blank=False, null=False)
    full_name = models.CharField(max_length=80, blank=False, null=False)
    email = models.EmailField(max_length=80, blank=False, null=False)
    password = models.CharField(max_length=255, blank=False, null=False)
    profile_picture = models.ImageField(upload_to='data/photos/', blank=True, null=True)
    date_of_birth = models.DateField(blank=False, null=False)

    def __str__(self):
        return self.username

class Veterinary(models.Model):
    TYPE_SERVICE = [
        ('domicilio', 'Domicílio'),
        ('clinica', 'Clínica'),
        ('ambos', 'Domicílio e Clínica'),
    ]
    full_name = models.CharField(max_length=80, blank=False, null=False)
    email = models.EmailField(max_length=80, blank=False, null=False)
    password_hash = models.CharField(max_length=255, blank=False, null=False)
    profile_picture = models.ImageField(upload_to='data/photos/', blank=True, null=True)
    date_of_birth = models.DateField(blank=False, null=False)
    cellphone = models.CharField(max_length=15, blank=False, null=False)
    crmv = models.CharField(max_length=10, unique=True, blank=False, null=False)
    date_crmv = models.DateField(blank=False, null=False)
    consult_value = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    description = models.CharField(max_length=250, blank=True, null=True)
    type_service = models.CharField(max_length=20, choices=TYPE_SERVICE, default="clinica", blank=False, null=False)

    def __str__(self):
        return self.crmv