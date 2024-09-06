#!/usr/bin/env python3
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple containing the input string k and the square
    of the input int/float v.

    Args:
    k (str): The input string.
    v (Union[int, float]): The input int or float.

    Returns:
    Tuple[str, float]: A tuple containing the input string k and the
    square of v as a float.
    """
    return k, float(v) ** 2
