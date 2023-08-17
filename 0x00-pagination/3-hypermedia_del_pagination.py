#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

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

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        The `get_hyper_index` function retrieves a subset of
        data from a dataset based on the given index and page size.

        :param index: The `index` parameter is an optional integer
                      that represents the starting index of the
                      data to retrieve.
        :type index: int
        :param page_size: The `page_size` parameter determines the
                          number of items to be returned in each
                          page of the dataset.
        :type page_size: int (optional)
        :return: The function `get_hyper_index` returns a dictionary
                 with the specified keys
        """
        self.dataset()
        idx_dataset = self.indexed_dataset()
        dataset_len = len(idx_dataset)

        if index is None:
            return None

        assert index < dataset_len
        start = index
        end = min(index + page_size, dataset_len)
        return {
            "index": index,
            "next_index": index + page_size if page_size < dataset_len
            else None,
            "page_size": page_size,
            "data": [idx_dataset.get(i) for i in range(start, end)]
        }
