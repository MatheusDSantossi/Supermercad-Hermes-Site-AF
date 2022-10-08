from django.contrib.auth.models import AbstractUser

from django.db import models

from django.core.validators import RegexValidator

# from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    bio = models.TextField(blank=True)
    # phone_number = PhoneNumberField(unique=True, null=False, blank=False)
    
    # esse phonenumber estava dando error com o phonenumber the alluser algo assim ai fiz o makemigrations dnv apos comentar
    # esses abaixo e deu certo
    
    # phoneNumberRegex = RegexValidator(regex = r"^\+?1\d{8, 15}$")
    # phoneNumber = models.CharField(validators= [phoneNumberRegex], max_length=16, unique=True, blank=True)
