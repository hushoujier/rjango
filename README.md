# Rjango

---

rjango is a tool that automatically generates up and down migration files for rust sqlx


- [Rjango](#rjango)
  - [Dependency](#dependency)
  - [Advantage](#advantage)
  - [Document](#document)
  - [Quick Start](#quick-start)
    - [create new project](#create-new-project)
    - [create python virtual environment](#create-python-virtual-environment)
    - [install rjango](#install-rjango)
    - [create .env file and set DATABASE\_URL](#create-env-file-and-set-database_url)
    - [rjango init](#rjango-init)
    - [rjango add](#rjango-add)
    - [sqlx migrate run](#sqlx-migrate-run)
    - [change model](#change-model)
    - [redo rjango add](#redo-rjango-add)
    - [redo sqlx migrate run](#redo-sqlx-migrate-run)
    - [sqlx migrate revert](#sqlx-migrate-revert)



## Dependency

---

* Python >= 3.10,<4



## Advantage

---

- **Convenient**: Automatically generate up and down migration files for Rust SQLx
- **Only development**: Although Rjango depends on the Python environment and the Django framework, it is only used during development. Upon release, there is no need to depend on Rjango, and there is also no runtime overhead
- **Bidirectional**: Rjango can not only convert Models into SQL TABLEs, but it can also reverse-engineer existing SQL TABLEs back into Models.
- **Multi-database support**: Sqlite、Postgre、Mysql

## Document

---

* [commnad line](https://github.com/hushoujier/rjango/blob/main/docs/command_line.md)
* [tutorial](https://github.com/hushoujier/rjango/blob/main/docs/tutorial.md)

## Quick Start

---

### create new project

```shell
cargo new rjango_example
code rjango_example
```

### create python virtual environment

```shell
rjango_example$ python -m venv venv
rjango_example$ source venv/bin/activate
rjango_example$ python --version
Python 3.10.11
```

### install rjango

```shell
rjango_example$ pip install rjango
```

### create .env file and set DATABASE_URL

```shell
rjango_example$ cat .env
DATABASE_URL=sqlite:////home/path/to/rjango_example/example.sqlite
```

### rjango init

```shell
rjango_example$ rjango init --example
```

A migrations folder with example Model files will be created.

```shell
rjango_example$ tree migrations/
migrations/
├── __init__.py
├── migrations
│   └── __init__.py
└── models
    ├── author.py
    ├── book.py
    ├── __init__.py
    ├── reader.py
    └── relations.py
```

### rjango add

```shell
rjango_example$ rjango add
```

generate up and down migration files for Rust SQLx

```shell
rjango_example$ tree migrations/
migrations/
├── 0001_created20250126.down.sql  # new
├── 0001_created20250126.up.sql    # new
├── __init__.py
├── migrations
│   ├── 0001_created20250126.py    # new
│   └── __init__.py
└── models
    ├── author.py
    ├── book.py
    ├── __init__.py
    ├── reader.py
    └── relations.py
```

```sqlite
rjango_example$ cat migrations/0001_created20250126.up.sql 
--
-- Create model Author
--
CREATE TABLE "example_author" ("author_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(64) NOT NULL UNIQUE);
--
-- Create model Reader
--
CREATE TABLE "example_reader" ("reader_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(64) NOT NULL UNIQUE);
--
-- Create model Book
--
CREATE TABLE "example_book" ("book_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(128) NOT NULL UNIQUE, "price" real NOT NULL, "description" text DEFAULT '' NULL, CONSTRAINT "example_book_check" CHECK ("price" >= 0.0));
--
-- Create model BookAuthorRelation
--
CREATE TABLE "example_book_author_relation" ("book_author_relation_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "publish_datetime" datetime NOT NULL, "author_id" bigint NOT NULL REFERENCES "example_author" ("author_id") DEFERRABLE INITIALLY DEFERRED, "book_id" bigint NOT NULL REFERENCES "example_book" ("book_id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model BookReaderRelation
--
CREATE TABLE "example_book_reader_relation" ("book_reader_relation_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "viewed_datetime" datetime NOT NULL, "book_id" bigint NOT NULL REFERENCES "example_book" ("book_id") DEFERRABLE INITIALLY DEFERRED, "reader_id" bigint NOT NULL REFERENCES "example_reader" ("reader_id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "example_book_author_relation_author_id_85d41095" ON "example_book_author_relation" ("author_id");
CREATE INDEX "example_book_author_relation_book_id_7d9100b8" ON "example_book_author_relation" ("book_id");
CREATE INDEX "example_book_reader_relation_book_id_3d79974d" ON "example_book_reader_relation" ("book_id");
CREATE INDEX "example_book_reader_relation_reader_id_646686e1" ON "example_book_reader_relation" ("reader_id");
```

```sqlite
rjango_example$ cat migrations/0001_created20250126.down.sql 
--
-- Create model BookReaderRelation
--
DROP TABLE "example_book_reader_relation";
--
-- Create model BookAuthorRelation
--
DROP TABLE "example_book_author_relation";
--
-- Create model Book
--
DROP TABLE "example_book";
--
-- Create model Reader
--
DROP TABLE "example_reader";
--
-- Create model Author
--
```

### sqlx migrate run

```shell
rjango_example$ sqlx migrate run
Applied 1/migrate created20250126 (2.030776ms)

rjango_example$ tree -L 1 .
.
├── Cargo.lock
├── Cargo.toml
├── example.sqlite   # new
├── migrations
├── src
├── target
└── venv
```

### change model

change `migrations/models/book.py`

```shell
# -*- coding:utf-8 -*-
from django.db import models


class Book(models.Model):
    """
    Book
    """
    book_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=512, unique=True, db_index=True) # max_length=128 change max_length=512
    price = models.FloatField()
    description = models.TextField(null=True, db_default='')
    viewed_numbers = models.IntegerField(null=True, db_default=0) # add viewed_numbers

    class Meta:
        """
        table config
        """
        db_table = 'example_book'
        constraints = [
            models.CheckConstraint(name='example_book_check', condition=models.Q(price__gte=0)),
        ]

```

### redo rjango add

```shell
rjango_example$ rjango add
```

```shell
rjango_example$ tree migrations/
migrations/
├── 0001_created20250126.down.sql
├── 0001_created20250126.up.sql
├── 0002_created20250126.down.sql     # new
├── 0002_created20250126.up.sql       # new
├── __init__.py
├── migrations
│   ├── 0001_created20250126.py
│   ├── 0002_created20250126.py       # new
│   └── __init__.py
└── models
    ├── author.py
    ├── book.py
    ├── __init__.py
    ├── reader.py
    └── relations.py
```

```sqlite
rjango_example$ cat migrations/0002_created20250126.up.sql 
--
-- Add field viewed_numbers to book
--
CREATE TABLE "new__example_book" ("viewed_numbers" integer DEFAULT 0 NULL, "book_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(128) NOT NULL UNIQUE, "price" real NOT NULL, "description" text DEFAULT '' NULL, CONSTRAINT "example_book_check" CHECK ("price" >= 0.0));
INSERT INTO "new__example_book" ("book_id", "name", "price", "description") SELECT "book_id", "name", "price", "description" FROM "example_book";
DROP TABLE "example_book";
ALTER TABLE "new__example_book" RENAME TO "example_book";
--
-- Alter field name on book
--
CREATE TABLE "new__example_book" ("book_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "price" real NOT NULL, "description" text DEFAULT '' NULL, "viewed_numbers" integer DEFAULT 0 NULL, "name" varchar(512) NOT NULL UNIQUE, CONSTRAINT "example_book_check" CHECK ("price" >= 0.0));
INSERT INTO "new__example_book" ("book_id", "price", "description", "viewed_numbers", "name") SELECT "book_id", "price", "description", "viewed_numbers", "name" FROM "example_book";
DROP TABLE "example_book";
ALTER TABLE "new__example_book" RENAME TO "example_book";
```

```sqlite
rjango_example$ cat migrations/0002_created20250126.down.sql 
--
-- Alter field name on book
--
CREATE TABLE "new__example_book" ("name" varchar(128) NOT NULL UNIQUE, "book_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "price" real NOT NULL, "description" text DEFAULT '' NULL, "viewed_numbers" integer DEFAULT 0 NULL, CONSTRAINT "example_book_check" CHECK ("price" >= 0.0));
INSERT INTO "new__example_book" ("book_id", "price", "description", "viewed_numbers", "name") SELECT "book_id", "price", "description", "viewed_numbers", "name" FROM "example_book";
DROP TABLE "example_book";
ALTER TABLE "new__example_book" RENAME TO "example_book";
--
-- Add field viewed_numbers to book
--
ALTER TABLE "example_book" DROP COLUMN "viewed_numbers";
```

### redo sqlx migrate run

```shell
rjango_example$ sqlx migrate run
Applied 2/migrate created20250126 (3.570937ms)
```

### sqlx migrate revert

```shell
rjango_example$ sqlx migrate revert --target-version 1
Applied 2/revert created20250126 (2.743494ms)
Skipped 1/revert created20250126 (0ns)
```