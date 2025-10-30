from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    name = models.CharField(max_length=50, null=False, verbose_name='Name of category')
    description = models.TextField(blank=True, verbose_name='Описание категории')

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products', verbose_name='Category')
    name = models.CharField(max_length=100, null=False, verbose_name='Product name')
    price = models.DecimalField(verbose_name='Price', max_digits=10, decimal_places=2)
    created = models.DateTimeField(verbose_name='Created at')
    available = models.BooleanField(default=True, verbose_name='В наличии')
    description = models.TextField(blank=True, verbose_name='Description')
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True, verbose_name='Изображение')
    average_rating = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    rating_votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

