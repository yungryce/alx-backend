#!/usr/bin/env python3
"""
Hypermedia pagination
"""
import csv
import math
from typing import Tuple, List, Dict, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple containing a start and end index.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: The start index and end index for the given page.
    """
    return ((page-1) * page_size, page_size * page)


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
        """return the appropriate page of the dataset"""
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        # get the data from the csv
        data = self.dataset()

        try:
            # get the index to start and end at
            start, end = index_range(page, page_size)
            return data[start:end]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """returns a dictionary containing the following key-value pairs
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        start, end = index_range(page, page_size)

        # estimating the next page
        if (page < total_pages):
            next_page = page+1
        else:
            next_page = None

        # estimating the previous page
        if (page == 1):
            prev_page = None
        else:
            prev_page = page - 1

        return {'page_size': len(data),
                'page': page,
                'data': data,
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': total_pages
                }
