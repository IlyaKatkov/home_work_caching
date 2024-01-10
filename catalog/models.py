from django.db import models
from django.conf import settings

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='наименование')
    description = models.TextField(**NULLABLE, verbose_name='описание')
    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(**NULLABLE, verbose_name='описание')
    picture = models.ImageField(upload_to='products/', verbose_name='превью', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена за покупку')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='авторизованный пользователь')
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'
    class Meta:
        permissions = [
            (
                'set_published_status',
                 'Can publish post'
            ),
            (
                'changing_the_description',
                'Can change the description'
            ),
            (
                'changing_the_category',
                'Can change the category'
            )
        ]
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('price',)


class Contact(models.Model):
    name = models.CharField(max_length=150, verbose_name='название')
    address = models.CharField(max_length=40, verbose_name='адрес')
    phone = models.CharField(max_length=10, verbose_name='телефон')
    email = models.EmailField(verbose_name='email')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    number_version = models.IntegerField(verbose_name='номер версии')
    name_version = models.CharField(max_length=100, verbose_name='название версии')
    version_indication = models.BooleanField(default=True, verbose_name='признак версии')

    def __str__(self):
        return f'{self.number_version} {self.name_version}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'