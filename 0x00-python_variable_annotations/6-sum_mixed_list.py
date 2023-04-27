#!/usr/bin/env python3
"""Script shows-> Type-annotated function sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Method; accepts a mixed list of integers & floats then returns
        their sum as float"""
    j: float = 0.0
    for y in mxd_lst:
        j += y
    return j
