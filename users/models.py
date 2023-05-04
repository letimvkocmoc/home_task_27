from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator
from django.db import models

from users.validators import check_birth_date, check_email


class Location(models.Model):
    name = models.CharField('Название', max_length=150, unique=True)
    lat = models.DecimalField('Латтитуда', max_digits=8, decimal_places=6, null=True, blank=True)
    lng = models.DecimalField('Лонгитуда', max_digits=8, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


class UserRoles(models.TextChoices):
    MEMBER = 'member', 'Пользователь'
    MODERATOR = 'moderator', 'Модератор'
    ADMIN = 'admin', 'Админ'


class User(AbstractUser):
    role = models.CharField(choices=UserRoles.choices, max_length=9, default=UserRoles.MEMBER)
    age = models.PositiveSmallIntegerField(null=True)
    location = models.ManyToManyField(Location)
    birth_date = models.DateField(validators=[check_birth_date], null=True)
    email = models.EmailField(unique=True, null=True, validators=[check_email])

    def save(self, *args, **kwargs):
        self.set_password(raw_password=self.password)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']
