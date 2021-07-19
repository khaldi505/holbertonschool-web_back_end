#!/usr/bin/env python3
from typing import List
"""
a type-annotated function sum_list which takes a
list input_list of floats as argument
"""


def sum_list(input_list: List[float]) -> float:
    """
    returns their sum as a float.
    """
    return sum(input_list)
