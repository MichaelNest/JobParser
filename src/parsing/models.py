from django.db import models
from .utils import *

class City(models.Model):
    name = models.CharField(max_length=55, verbose_name='Название города', unique=True)
    slug = models.CharField(max_length=55, blank=True, unique = True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyr_to_lat(str(self.name))
        super().save(*args, **kwargs)


    class Meta:
        verbose_name='Город'
        verbose_name_plural = 'Города'

class Language(models.Model):
    name = models.CharField(max_length=55, unique=True, verbose_name='Язык программирования')
    slug = models.CharField(max_length=55, blank=True, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyr_to_lat(str(self.name))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name='Язык программирования'
        verbose_name_plural= 'Языки программирования'