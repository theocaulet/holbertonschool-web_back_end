#!/usr/bin/env python3
"""
This module contains a function task_wait_random that takes an integer
max_delay and returns a asyncio.Task that is an instance of wait_random
(max_delay).
"""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Takes an integer max_delay and returns a asyncio.Task that is an
    instance of wait_random(max_delay)."""
    return asyncio.create_task(wait_random(max_delay))
