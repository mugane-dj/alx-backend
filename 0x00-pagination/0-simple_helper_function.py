#!/usr/bin/env python3
"""
Simple helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    The function `index_range` takes in a page number and page size
    and returns the start and end indices for that page.

    :param page: The `page` parameter represents the current page number.
    :type page: int
    :param page_size: The `page_size` parameter represents the number of
                      items per page.
    :type page_size: int
    :return: a tuple containing the start index and end index of a given
             page and page size.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
