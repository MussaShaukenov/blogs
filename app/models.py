from django.db import models


class Cards(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()

    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'
        db_table = 'cards'
