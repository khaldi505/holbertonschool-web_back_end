#!/usr/bin/env python3
""""
type-annotated function make_multiplier
that takes a float multiplier as argument
returns a function that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ return a callable """
    def multiply(x: float) -> float:
        """return x * multiplier :')"""
        return x * multiplier
    return multiply
