# -*- coding:utf-8 -*-
"""
@Time             : 2025-01-24
@Email            : hushoujier@qq.com
@Author           : 胡守杰
@FileName         : common.py
@ZhDescription    :
@EnDescription    :
"""
import os
from pathlib import Path


def get_target() -> str:
    """
    Migrate files to save folders
    """
    target = os.environ.get('RJANGO_TARGET', os.path.join(os.getcwd(), 'migrations'))
    if not target.endswith('migrations'):
        raise RuntimeError('The environment variable RJANGO_TARGET must end with migrations')
    return target


def get_base_dir() -> Path:
    """
    core base dir
    """
    return Path(get_target()).parent
