#!/usr/bin/env python3
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the input multiplier.

    Args:
    multiplier (float): The input multiplier.

    Returns:
    Callable[[float], float]: A function that takes a float and returns
    the product of the input float and the multiplier.
    """
    def multiply(x: float) -> float:
        return x * multiplier
    return multiply
