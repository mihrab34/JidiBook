# from django.contrib.auth.models import AbstractUser, PermissionsMixin
# from django.core.validators import RegexValidator
# from django.db import models

# phone_validator = RegexValidator(
#     r"^(\+?\d{0,4})?\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{4}\)?)?$",
#     "The phone number provided is invalid",
# )


# class User(AbstractUser, PermissionsMixin):
#     email = models.EmailField(max_length=100, unique=True)
#     phone_number = models.CharField(max_length=16, validators=[phone_validator], unique=True)
#     full_name = models.CharField(max_length=30)
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)


#     is_staff = models.BooleanField(default=False)

#     def __str__(self):
#         return self.email

#     @staticmethod
#     def has_perm(perm, obj=None, **kwargs):
#         return True

#     @staticmethod
#     def has_module_perms(app_label, **kwargs):
#         return True

#     @property
#     def is_staff(self):
#         return self.is_admin
