#!/usr/bin/env python3
""" str and int to tuple """
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """to_kv"""

    return (k, v**2)
