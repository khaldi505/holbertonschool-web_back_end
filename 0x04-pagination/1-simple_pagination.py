#!/usr/bin/env python3
"""
nyes
"""
import csv
import math
from typing import List


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

    def index_range(self, page: int, page_size: int) -> tuple:
        """a function that"""
        return ((page * page_size - page_size), (page * page_size))

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get page
        """
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0
        indx = self.index_range(page, page_size)
        start = indx[0]
        end = indx[1]
        x = start
        result = []
        csv_file = self.dataset()
        if len(csv_file) < end:

            return []

        while start != end:
            result.append(csv_file[start])
            start += 1

        return result
