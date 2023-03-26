from django.db import models
from django.utils import timezone


class Categories(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = 'categories'


class Cards(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'
        db_table = 'cards'

