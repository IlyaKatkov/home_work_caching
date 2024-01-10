from django.db import models
from django.contrib.auth.models import AbstractUser
from catalog.models import NULLABLE

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')


    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    country = models.CharField(max_length=40, verbose_name='страна')
    is_active = models.BooleanField(default=False, verbose_name='статус активности')
    email_verificator = models.CharField(max_length=25, **NULLABLE, verbose_name='код верификации почты')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
