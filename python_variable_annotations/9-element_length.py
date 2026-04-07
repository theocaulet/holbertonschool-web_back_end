#!/usr/bin/python3
"""
This module contains a function that takes a list of sequences
and returns a list of tuples with each sequence and its length.
"""
import typing


def element_length(lst: typing.Iterable[typing.Sequence]) -> typing.List[
        typing.Tuple[typing.Sequence, int]]:
    """Returns a list of tuples wich each sequence and its length."""
    return [(i, len(i)) for i in lst]
