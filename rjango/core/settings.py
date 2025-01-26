# -*- coding:utf-8 -*-
"""
@Time             : 2025-01-24
@Email            : hushoujier@qq.com
@Author           : 胡守杰
@FileName         : settings.py
@ZhDescription    :
@EnDescription    :
"""
import os

import environ
import rich
import typer

from rjango.utils.common import get_base_dir

__all__ = ['SETTINGS']

env = environ.Env()
environ.Env.read_env(os.path.join(str(get_base_dir()), '.env'))
databases = env.db('DATABASE_URL', {})
if not databases:
    rich.print('[Error] the .env file must contain the DATABASE_URL')
    raise typer.Abort()

SETTINGS = {
    'BASE_DIR': get_base_dir(),
    'INSTALLED_APPS': [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'migrations',
    ],
    'DATABASES': {'default': databases},
}
