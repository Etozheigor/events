from django.contrib.auth import get_user_model
from django.db import models
from django.utils.safestring import mark_safe
import os.path


User = get_user_model()


class Organization(models.Model):
    """Модель организаций."""

    title = models.CharField(verbose_name='Название', max_length=200)
    description = models.CharField(verbose_name='Описание', max_length=500)
    address = models.CharField(verbose_name='Адрес', max_length=200)
    postcode = models.IntegerField(verbose_name='Почтовый индекс')

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'

    def __str__(self):
        return self.title


class Event(models.Model):
    """Модель мероприятий."""
    title = models.CharField(verbose_name='Название', max_length=200)
    description = models.CharField(verbose_name='Описание', max_length=500)
    organizations = models.ManyToManyField(
        Organization, verbose_name='Организации', related_name='organizations')
    image = models.ImageField()
    date = models.DateTimeField(verbose_name='Дата')

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return self.title
    
    def image_tag(self):
        if self.image:
            # print(os.path.abspath(os.curdir))
            # print(os.path.abspath(__file__))
            print(os.path.isfile("C:\Dev\events\events_project\media\\temp_bBDm4qJ.png"))
            # print(mark_safe(f'<img src="{self.image.url}" style="width: 45px; height:45px;" />'))
            # return mark_safe(f'<img src="{self.image.url}" style="width: 45px; height:45px;" />')
            print(mark_safe('<img src="C:\Dev\events\events_project\media\\temp_bBDm4qJ.png" style="width: 45px; height:45px;" />'))
            return mark_safe('<img src="C:\Dev\events\events_project\media\\temp_bBDm4qJ.png" style="width: 45px; height:45px;" />')
        else:
            return 'No Image Found'
    image_tag.short_description = 'Изображение'