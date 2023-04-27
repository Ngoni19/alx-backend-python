#!/usr/bin/env python3
"""Script shows - > Type-annotated function element_length"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Method: Returns a list of tuples of sequence & int"""
    return [(i, len(i)) for i in lst]
