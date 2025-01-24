# -*- coding:utf-8 -*-
"""
@Time             : 2025-01-24
@Email            : hushoujier@qq.com
@Author           : 胡守杰
@FileName         : decorators.py
@ZhDescription    :
@EnDescription    :
"""
import sys
from functools import wraps
from typing import Callable

from rjango.utils import get_base_dir
from rjango.core.setup import setup


def setup_django(function: Callable) -> Callable:
    """
    setup_django
    """

    @wraps(function)
    def inner(*args, **kwargs):
        sys.path.insert(0, str(get_base_dir()))
        setup()
        function(*args, **kwargs)

    return inner
