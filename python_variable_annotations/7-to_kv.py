#!/usr/bin/python3
"""
This module contains a function that takes a string k
and a value v which can be an integer of a float as arguments
and returns a tuple.
"""
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """Returns a tuple."""
    return (k, float(v ** 2))
