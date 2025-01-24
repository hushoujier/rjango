# -*- coding:utf-8 -*-
"""
@Time             : 2025-01-24
@Email            : hushoujier@qq.com
@Author           : 胡守杰
@FileName         : setup.py
@ZhDescription    :
@EnDescription    :
"""
import django
from django.conf import settings

from rjango.core.settings import SETTINGS


def setup():
    """
    setup core
    """
    settings.configure(**SETTINGS)
    django.setup()
