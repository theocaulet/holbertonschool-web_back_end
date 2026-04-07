#!/usr/bin/env python3
"""
This module contains a function that sums a list of integers and floats
and returns the result as a float.
"""
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """Sums a list of integers and floats and return the result as a float."""
    return sum(mxd_lst)
