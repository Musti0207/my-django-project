from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    gender = models.CharField(
        max_length=10,
        choices=[('male', 'Erkek'), ('female', 'Kadın'), ('other', 'Diğer')],
        blank=True,
        null=True
    )
    is_seller = models.BooleanField(default=False)  # Satıcı mı?
    is_customer = models.BooleanField(default=True)  # Müşteri mi?

    def __str__(self):
        return self.username
