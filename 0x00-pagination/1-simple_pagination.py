#!/usr/bin/env python3
"""
Simple helper function
"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """
    return a tuple of size two containing a start
    index and an end index corresponding to the range
    of indexes to return in a list for those particular
    pagination parameters
    """
    start_index = page_size * (page - 1)
    end_index = start_index + page_size
    return (start_index, end_index)


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
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        try:
            type_er = "raised when page and/or page_size are not ints"
            assert isinstance(page, int), type_er
            assert isinstance(page_size, int), type_er
            assert page != 0 and page_size != 0, "raised with 0"
            assert page > 0 and page_size > 0, "raised with negative values"
        except AssertionError as e:
            print(f"AssertionError {e}")
            return []
        range = index_range(page, page_size)
        if (range[0] >= len(self.dataset()) or
                range[1] >= len(self.dataset())):
            return []
        return self.dataset()[range[0]: range[1]]
