#!/usr/bin/env python3
"""
This module contains a coroutine called async_comprehension that collects
10 random numbers using an async comprehensing over async_generator,
and returns the 10 random numbers.
"""


import typing
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """Collects 10 random numbers using an async comprehensing over
    async_generator, and returns the 10 random numbers."""
    return [i async for i in async_generator()]
