from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, phone, email, full_name=None, password=None):
        if not phone:
            raise ValueError("Phone number is required")
        if not full_name:
            raise ValueError("Full name is required")
        user = self.model(phone=phone, email=self.normalize_email(email), full_name=full_name)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, full_name=None, password=None):
        user = self.create_user(
            phone=phone,
            full_name=full_name,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    phone_validator = RegexValidator(
        r"^(\+?\d{0,4})?\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{4}\)?)?$",
        "The phone number provided is invalid",
    )
    phone = models.CharField(max_length=16, validators=[phone_validator], unique=True)
    email = models.EmailField(max_length=70, unique=True, blank=True, null=True)
    full_name = models.CharField(max_length=30)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["full_name", "password"]

    def __str__(self):
        return self.full_name

    def has_perm(perm, obj=None, **kwargs):
        return True

    @staticmethod
    def has_module_perms(app_label, **kwargs):
        return True

    @property
    def is_staff(self):
        return self.is_admin
