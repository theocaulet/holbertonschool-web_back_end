#!/usr/bin/env python3
"""
This module contains a function task_wait_n that takes in two integers,
n and max_delay, and returns a list of all the delays (float values)
of the n coroutines created by wait_random(max_delay), in the order
they are completed.
"""
import asyncio
import typing
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """Takes in two integers, n and max_delay, and returns a list of
    all the delays (float values) of the n coroutines created by
    wait_random(max_delay), in the order they are completed."""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []
    for Tasks in asyncio.as_completed(tasks):
        delay = await Tasks
        delays.append(delay)
    return delays
