#!/usr/bin/env python3
"""
This module provides a helper function for pagination.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple containing a start index and an end index
    corresponding to the range of indexes to return in a list for the
    given pagination parameters.

    Parameters:
    - page (int): The current page number (1-indexed).
    - page_size (int): The number of items per page.

    Returns:
    - Tuple[int, int]: A tuple of two integers representing the start
      index and end index.
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
