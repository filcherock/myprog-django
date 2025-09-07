from django.db import models
from django_resized import ResizedImageField
from django.utils import timezone

class App(models.Model):
    icon = ResizedImageField (
        verbose_name='Иконка программы',
        force_format='WEBP',
        quality=75,
        upload_to='apps',
    )

    id = models.IntegerField(verbose_name='ID', default=0, primary_key=True)
    bg = models.CharField(verbose_name='Цвет заднего фона')
    title = models.CharField(verbose_name='Название программы', max_length=50)
    descriptions = models.TextField(verbose_name='Описание')
    version = models.CharField(verbose_name='Текущая версия')
    winplatform = models.BooleanField(verbose_name='Поддержка Windows', default=True)
    linuxplatform = models.BooleanField(verbose_name='Поддержка Linux', default=True)
    reliases = models.DateField(verbose_name='Релиз', default=timezone.now)
    author = models.TextField(verbose_name='Автор', default='filcher')
    verAuthor = models.BooleanField(verbose_name='Верифицированный автор', default=False)
    opensource = models.BooleanField(verbose_name='Open-Source проект', default=True)
    fileSetup = models.FileField(verbose_name="Файл установщик")
    githubSite = models.TextField(verbose_name='Ссылка на GitHub', default='https://github.com')
    screenshotes = models.BooleanField(verbose_name='Есть ли скрриншоты?', default=True)
    screen1 = models.ImageField (
        verbose_name='Скрин 1',
        upload_to='screens',
        default="sus.png"
    )
    screen2 = models.ImageField (
        verbose_name='Скрин 2',
        upload_to='screens',
        default="sus.png"
    )
    screen3 = models.ImageField (
        verbose_name='Скрин 3',
        upload_to='screens',
        default="sus.png"
    )

    class Meta:
        verbose_name = 'Приложения'
        verbose_name_plural = 'Приложения'
    
    def __str__(self):
        return self.title