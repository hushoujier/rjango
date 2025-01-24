# -*- coding:utf-8 -*-
"""
@Time             : 2025-01-24
@Email            : hushoujier@qq.com
@Author           : 胡守杰
@FileName         : schema.py
@ZhDescription    :
@EnDescription    :
"""

from django.core.exceptions import ImproperlyConfigured

__all__ = ['SCHEMA_MAPPING']

SCHEMA_MAPPING = {}

try:
    import django.db.backends.sqlite3.base
    from django.db.backends.sqlite3.schema import DatabaseSchemaEditor as BaseSqlite3SchemaEditor
except ImproperlyConfigured:
    pass
else:
    class Sqlite3SchemaSchemaEditor(BaseSqlite3SchemaEditor):
        """
        Custom generated SQL statements
        """


    SCHEMA_MAPPING[django.db.backends.sqlite3.base.DatabaseWrapper.vendor] = Sqlite3SchemaSchemaEditor

try:
    import django.db.backends.postgresql.base
    from django.db.backends.postgresql.schema import DatabaseSchemaEditor as BasePostgresqlSchemaEditor
except ImproperlyConfigured:
    pass
else:
    class PostgresqlSchemaEditor(BasePostgresqlSchemaEditor):
        """
        Custom generated SQL statements
        """


    SCHEMA_MAPPING[django.db.backends.postgresql.base.DatabaseWrapper.vendor] = PostgresqlSchemaEditor

try:
    import django.db.backends.mysql.base
    from django.db.backends.mysql.schema import DatabaseSchemaEditor as BaseMysqlSchemaEditor
except ImproperlyConfigured:
    pass
else:

    class MysqlSchemaEditor(BaseMysqlSchemaEditor):
        """
        Custom generated SQL statements
        """


    SCHEMA_MAPPING[django.db.backends.mysql.base.DatabaseWrapper.vendor] = MysqlSchemaEditor

try:
    import django.db.backends.oracle.base

    from django.db.backends.oracle.schema import DatabaseSchemaEditor as BaseOracleSchemaEditor
except ImproperlyConfigured:
    pass
else:
    class OracleSchemaEditor(BaseOracleSchemaEditor):
        """
        Custom generated SQL statements
        """


    SCHEMA_MAPPING[django.db.backends.oracle.base.DatabaseWrapper.vendor] = OracleSchemaEditor
