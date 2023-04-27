#!/usr/bin/env python3
"""Script shows -> Advanced type annotated function"""
from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')

def safely_get_value(
    dct: Mapping[str, Any], key: str, default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Returns the value in the dictionary with the given key, or the default value
    if the key is not present.
    """
    return dct.get(key, default)
