from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Account(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    phone_number = PhoneNumberField(unique=True)

    def __str__(self):
        return self.username
