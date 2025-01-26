# turorial

---


- [turorial](#turorial)
  - [Support DATABASE\_URL format](#support-database_url-format)
  - [Support Model fields](#support-model-fields)
  - [Support Model Meta options](#support-model-meta-options)
  - [How to use  completion when writing Model](#how-to-use--completion-when-writing-model)
  - [How to reverse existing SQL TABLEs back into Models](#how-to-reverse-existing-sql-tables-back-into-models)
    - [1. create .env file and set DATABASE\_URL for existing database](#1-create-env-file-and-set-database_url-for-existing-database)
    - [2. inspect existing database](#2-inspect-existing-database)




## Support DATABASE_URL format

* PostgreSQL: ``postgres[ql]?://`` or ``p[g]?sql://``
* PostGIS: ``postgis://``
* MySQL: ``mysql://`` or ``mysql2://``
* MySQL (GIS): ``mysqlgis://``
* MySQL Connector Python from Oracle: ``mysql-connector://``
* SQLite: ``sqlite://``
* SQLite with SpatiaLite for GeoDjango: ``spatialite://``
* Oracle: ``oracle://``
* Microsoft SQL Server: ``mssql://``
* PyODBC: ``pyodbc://``
* Amazon Redshift: ``redshift://``
* LDAP: ``ldap://``



## Support Model fields

---

[Model field reference](https://docs.djangoproject.com/en/5.1/ref/models/fields/)



## Support Model Meta options

---

[Model `Meta` options](https://docs.djangoproject.com/en/5.1/ref/models/options/)



## How to use  completion when writing Model

---

Install VSCode `python` and `Django` extension



## How to reverse existing SQL TABLEs back into Models

---

### 1. create .env file and set DATABASE_URL for existing database

```ini
DATABASE_URL=[existing database url]
```

### 2. inspect existing database

```shell
rjango init --no-example
rjango inspect
```

The Model was created in `migrations/models/__init__.py`. example:

```python
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ExampleAuthor(models.Model):
    author_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=64)

    class Meta:
        db_table = 'example_author'


class ExampleBook(models.Model):
    book_id = models.AutoField(primary_key=True)
    price = models.FloatField()
    description = models.TextField(blank=True, null=True)
    viewed_numbers = models.IntegerField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=512)

    class Meta:
        db_table = 'example_book'


class ExampleBookAuthorRelation(models.Model):
    book_author_relation_id = models.AutoField(primary_key=True)
    publish_datetime = models.DateTimeField()
    author_id = models.ForeignKey(ExampleAuthor, models.DO_NOTHING, db_column='author_id')
    book_id = models.ForeignKey(ExampleBook, models.DO_NOTHING, db_column='book_id')

    class Meta:
        db_table = 'example_book_author_relation'


class ExampleBookReaderRelation(models.Model):
    book_reader_relation_id = models.AutoField(primary_key=True)
    viewed_datetime = models.DateTimeField()
    book_id = models.ForeignKey(ExampleBook, models.DO_NOTHING, db_column='book_id')
    reader_id = models.ForeignKey('ExampleReader', models.DO_NOTHING, db_column='reader_id')

    class Meta:
        db_table = 'example_book_reader_relation'


class ExampleReader(models.Model):
    reader_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=64)

    class Meta:
        db_table = 'example_reader'

```





