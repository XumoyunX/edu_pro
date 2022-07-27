# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.utils.translation import gettext_lazy as _
#
#
# class User(AbstractUser):
#     email = models.EmailField(_('email address'), unique=True)
#





from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    photo = models.ImageField()

    # USERNAME_FIELD = 'email'
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username']





