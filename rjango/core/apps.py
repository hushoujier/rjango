# -*- coding:utf-8 -*-
"""
@Time             : 2025-01-24
@Email            : hushoujier@qq.com
@Author           : 胡守杰
@FileName         : apps.py
@ZhDescription    :
@EnDescription    :
"""
from django.apps import AppConfig


class MigrationsConfig(AppConfig):
    """
    MigrationsConfig
    """
    default_auto_field = 'core.db.models.BigAutoField'
    name = 'migrations'
