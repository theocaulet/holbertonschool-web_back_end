#!/usr/bin/env python3
"""
This module contains an asynchronous function that waits for a random delay
between 0 and a specified maximum delay, then returns the actual delay.
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random delay between 0 and max_delay seconds, then returns
    the actual delay."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
