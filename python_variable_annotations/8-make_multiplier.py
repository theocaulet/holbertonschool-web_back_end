#!/usr/bin/env python3
"""
This module contains a function that takes a float multiplier as argument
and returns a function that multiplies a float by multiplier.
"""
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier."""
    def multiply(number: float) -> float:
        """Returns the product of multiplier and number."""
        return multiplier * number
    return multiply
