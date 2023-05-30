from django.contrib.auth.models import AbstractUser
from django.db import models

from events.models import Organization


class User(AbstractUser):
    """Модель пользователя."""

    username = models.CharField('Логин', unique=True, max_length=150)
    email = models.EmailField('email', unique=True, max_length=150)
    organization = models.ForeignKey(
        Organization, null=True,
        on_delete=models.SET_NULL, related_name='users')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
