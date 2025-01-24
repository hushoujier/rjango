# -*- coding:utf-8 -*-

from django.db import models

from migrations.models.author import Author
from migrations.models.book import Book
from migrations.models.reader import Reader


class BookAuthorRelation(models.Model):
    """
    BookAuthorRelation
    """
    book_author_relation_id = models.BigAutoField(primary_key=True)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, db_column='book_id')
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE, db_column='author_id')
    publish_datetime = models.DateTimeField()

    class Meta:
        """
        table config
        """
        db_table = 'example_book_author_relation'


class BookReaderRelation(models.Model):
    """
    BookReaderRelation
    """
    book_reader_relation_id = models.BigAutoField(primary_key=True)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, db_column='book_id')
    reader_id = models.ForeignKey(Reader, on_delete=models.CASCADE, db_column='reader_id')
    viewed_datetime = models.DateTimeField()

    class Meta:
        """
        table config
        """
        db_table = 'example_book_reader_relation'
