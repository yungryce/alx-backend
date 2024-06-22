#!/usr/bin/env python3
"""Simple pagination
"""

import csv
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.

    Attributes:
        DATA_FILE (str): The name of the CSV file containing the data.
        __dataset (List[List]): A cached list of the dataset.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the Server instance with an empty dataset."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset.

        Reads the dataset from a CSV file if it hasn't been loaded already.

        Returns:
            List[List]: The loaded dataset without the header row.
        """
        if self.__dataset is None:
            # Open the CSV file and read its contents.
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            # Cache the dataset excluding the header row.
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Finds the correct indexes to paginate dataset.

        Args:
            page (int): The page number to retrieve (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            List[List]: A list of rows corresponding to the requested page.
        """
        # Ensure page and page_size are valid positive integers.
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0

        # Get the size of the dataset.
        csv_size = len(self.dataset())

        # Calculate the start and end indices for the requested page.
        start, end = index_range(page, page_size)

        # Adjust the end index to not exceed the dataset size.
        end = min(end, csv_size)

        # If the start index is beyond the dataset size, return an empty list.
        if start >= csv_size:
            return []

        # Return the subset of the dataset for the requested page.
        return self.dataset()[start:end]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple containing a start and end index.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: The start index and end index for the given page.
    """
    return ((page - 1) * page_size, page * page_size)
