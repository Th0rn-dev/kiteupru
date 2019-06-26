from django.db import models

# Create your models here.

class Page(models.Model):
    """Сраница основного раздела сайта kiteup.ru"""
    title = models.CharField(default='', max_length=80)
    link = models.CharField(default='', max_length=50)
    body = models.TextField('Content', default='')

    def __str__(self):
        return self.link

    class Meta:
        verbose_name = 'Страницы'
        verbose_name_plural = 'Статические страницы'