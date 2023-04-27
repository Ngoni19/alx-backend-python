#!/usr/bin/env python3
"""Script shows - > Type-annotated function to_kv"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Method: Returns tuple of a str & float"""
    y = v ** 2
    return (k, y)
