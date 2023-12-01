from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Materials(models.Model):
    title = models.CharField(max_length=20, verbose_name='заголовок')
    slug = models.CharField(max_length=100, verbose_name='slug', **NULLABLE)
    content = models.TextField(verbose_name='содержимое')
    picture = models.ImageField(upload_to='bloging/', verbose_name='превью', **NULLABLE)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    views_count = models.IntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return f'{self.title}'
    class Meta:
        verbose_name = 'материал'
        verbose_name_plural = 'материалы'
