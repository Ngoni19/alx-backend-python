#!/usr/bin/env python3
"""Script shows -> Defines duck typed function"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Method: The types of the elements of the input are not known"""
    if lst:
        return lst[0]
    else:
        return None
