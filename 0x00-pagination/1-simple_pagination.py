#!/usr/bin/env python3
"""
This module provides a Server class
to paginate a dataset of popular baby names.
"""

import csv
import math
from typing import List, Tuple


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a page of the dataset corresponding
        to the given pagination parameters.

        Parameters:
        - page (int): The current page number (default is 1).
        - page_size (int): The number of items per page (default is 10).

        Returns:
        - List[List]: A list of rows corresponding to the current page.
        """
        assert isinstance(page, int) and page > 0, "Page number must
        be a positive integer."
        assert isinstance(page_size, int) and page_size > 0, "Page size must
        be a positive integer."

        start, end = index_range(page, page_size)
        dataset = self.dataset()

        if start >= len(dataset):
            return []  "Return an empty list
        if the start index is out of range"

        return dataset[start:end]
