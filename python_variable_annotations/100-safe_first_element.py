#!/usr/bin/env python3
from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Returns the first element of the input list if it is not empty,
    otherwise returns None.

    Args:
    lst (Sequence[Any]): The input list.

    Returns:
    Optional[Any]: The first element of the input list, or None if the
    list is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
