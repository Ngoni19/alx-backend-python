#!/usr/bin/env python3
"""Script shows -> Type-annotated function make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Method: Returns a function that multiplies the float"""
    return lambda y: y * multiplier
