# -*- coding:utf-8 -*-
from django.db import models


class Book(models.Model):
    """
    Book
    """
    book_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=128, unique=True, db_index=True)
    price = models.FloatField()
    description = models.TextField(null=True, db_default='')

    class Meta:
        """
        table config
        """
        db_table = 'example_book'
        constraints = [
            models.CheckConstraint(name='example_book_check', condition=models.Q(price__gte=0)),
        ]
