from django.db import models
from .utils import *
from django.utils.text import slugify

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

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.name)
    #     super().save(*args, **kwargs)

    class Meta:
        verbose_name='Язык программирования'
        verbose_name_plural= 'Языки программирования'

class Vacancy(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=555, verbose_name='Заголовок вакансии')
    company = models.CharField(max_length=222, verbose_name='Компания')
    description = models.TextField(verbose_name='Описание вакансии')
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name='Язык программирования')
    create_time = models.DateField(auto_now_add=True, verbose_name='Дата обьявления')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'