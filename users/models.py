from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password

class CustomUser(AbstractUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

    def save(self, *args, **kwargs):
        if self.pk is None or 'password' in self.get_deferred_fields():
            self.password = make_password(self.password)
        super().save(*args, **kwargs)