# -*- coding:utf-8 -*-
from django.db import models


class Reader(models.Model):
    """
    Reader
    """
    reader_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=64, unique=True, db_index=True)

    class Meta:
        """
        table config
        """
        db_table = 'example_reader'
