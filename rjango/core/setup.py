# -*- coding:utf-8 -*-
"""
@Time             : 2025-01-24
@Email            : hushoujier@qq.com
@Author           : 胡守杰
@FileName         : setup.py
@ZhDescription    :
@EnDescription    :
"""


def setup():
    """
    setup core
    """
    import django
    from django.conf import settings
    from rjango.core.settings import SETTINGS
    settings.configure(**SETTINGS)
    django.setup()
