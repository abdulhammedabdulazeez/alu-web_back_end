#!/usr/bin/env python3
from typing import List, Any, Tuple


def element_length(lst: List[Any]) -> List[Tuple[Any, int]]:
    """
    Returns a list of tuples, where each tuple contains an element
    from the input list and its length.

    Args:
    lst (List[Any]): The input list.

    Returns:
    List[Tuple[Any, int]]: A list of tuples, where each tuple contains
    an element from the input list and its length.
    """
    return [(i, len(i)) for i in lst]
