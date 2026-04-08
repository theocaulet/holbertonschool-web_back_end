#!/usr/bin/env python3
"""
This module contains an asynchronous function that takes in two integers,
n and max_delay, and returns a list of all the delays (float values)
of the n coroutines created by wait_random(max_delay), in the order they are
completed.
"""
import asyncio
import typing
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """Takes in two integers, n and max_delay, and returns a list of
      all the delays (float values) of the n coroutines created by
      wait_random(max_delay),
      in the order they are completed."""
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []
    for coroutine in asyncio.as_completed(tasks):
        delay = await coroutine
        delays.append(delay)
    return delays
