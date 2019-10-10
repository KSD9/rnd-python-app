from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


class BeerModel(models.Model):
    class Meta:
        verbose_name_plural = "Beers"

    def __str__(self):
        return self.name

    BEER_TYPE_CHOICES = [
        ('AL', 'Ale'),
        ('LA', 'Lager'),
        ('ST', 'Stout'),
    ]

    beer_type = models.CharField(
        max_length=2,
        choices=BEER_TYPE_CHOICES,
        default='LA')

    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)


class WhiskeyModel(models.Model):
    brand = models.CharField(max_length=50, blank=False, null=False)
    age = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)],
                                      blank=False, null=False)
    description = models.CharField(max_length=500, blank=False, null=False)
