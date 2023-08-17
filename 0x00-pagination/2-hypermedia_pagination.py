#!/usr/bin/env python3
"""
Hypermedia pagination
"""
from typing import Tuple, List, Dict
import csv
import math


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


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        The `get_page` function retrieves a specific page of data from a
        dataset, based on the given page number and page size.

        :param page: The `page` parameter is an integer that represents
                     the page number of the dataset you want to retrieve.
        :type page: int (optional)
        :param page_size: The `page_size` parameter determines the number
                          of items that will be displayed on each page.
        :type page_size: int (optional)
        :return: a list of lists.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        idx_range = index_range(page, page_size)
        offset = idx_range[0]
        end_index = idx_range[-1]
        self.dataset()
        return self.__dataset[offset:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        The function `get_hyper` returns a dictionary containing information
        about a paginated dataset

        :param page: The `page` parameter is used to specify the current
                     page number.
        :type page: int (optional)
        :param page_size: The `page_size` parameter determines the number
                          of items or records to be displayed on each page
                          of the dataset.
        :type page_size: int (optional)
        :return: a dictionary with the specified keys and values:
        """
        self.dataset()
        total_lists = len(self.__dataset)
        total_pages = math.ceil(total_lists / page_size)
        if page <= 1:
            prev_page = None
        else:
            prev_page = page - 1

        if page >= total_pages:
            next_page = None
        else:
            next_page = page + 1

        return {
            "page_size": page_size,
            "page": page,
            "data": self.get_page(page=page, page_size=page_size),
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
