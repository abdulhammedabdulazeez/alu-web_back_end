#!/usr/bin/env python3
from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Returns the value associated with the input key in the input
     dictionary, or the default value if the key is not in the
     dictionary.

    Args:
    dct (Mapping): The input dictionary.
    key (Any): The input key.
    default (Union[T, None], optional): The default value to return
    if the key is not in the dictionary. Defaults to None.

    Returns:
    Union[Any, T]: The value associated with the input key in the input
     dictionary, or the default value if the key is not in the
     dictionary.
    """
    if key in dct:
        return dct[key]
    else:
        return default
