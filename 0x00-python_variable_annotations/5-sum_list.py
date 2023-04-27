#!/usr/bin/env python3
"""Script shows - > Type-annotated function sum_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Method: takes a list of floats  returns their sum as float"""
    j: float = 0.0
    for i in input_list:
        j += i
    return j
