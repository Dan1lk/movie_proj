from django.db import models
from django.urls import  reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    director_email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_url(self):
        return reverse('one_dir', args=[self.id])

class Actor(models.Model):
    MALE = "M"
    FEMALE = "F"
    GENDERS = [
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    gender = models.CharField(max_length=1, choices=GENDERS, default=MALE)

    def __str__(self):
        if self.gender == self.MALE:
            return f'Актер {self.first_name} {self.last_name}'
        else:
            return f'Актрисса {self.first_name} {self.last_name}'

    def get_url(self):
        return reverse('one_act', args=[self.id])
class Movie(models.Model):
    EURO = "EUR"
    USD = "USD"
    RUB = "RUB"
    CURRENCY_CHOICES = [
        (EURO, 'EURO'),
        (USD, 'Dollars'),
        (RUB, 'Rubles'),
    ]

    name = models.CharField(max_length=40)
    rating = models.IntegerField(validators=[MinValueValidator(1),
                                             MaxValueValidator(100)])
    year = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(default=1000000, blank=True, validators=[MinValueValidator(1)])
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=RUB)
    slug = models.SlugField(default='', null=False)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True)
    actors = models.ManyToManyField(Actor)

    def get_url(self):
        return reverse('movie-detail', args=[self.slug])

    def __str__(self):
        return f'{self.name}-{self.rating}%'