#!/usr/bin/env python3
"""Script Type-annotated function add"""

from typing import List

def add_numbers(numbers: List[float]) -> float:
    """Takes a list of two floats and returns their sum as a float"""
    if len(numbers) != 2:
        raise ValueError("Function requires exactly 2 float arguments")
    return sum(numbers)
