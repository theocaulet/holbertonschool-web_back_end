#!/usr/bin/env python3
"""
This module contains an asynchronous generator that yields a random
float between 0 and 10 every second for 10 seconds.
"""


import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Yields a random float between 0 and 10 every second for
    10 seconds.
    """
    for _ in range(10):
        await asyncio.sleep(1)
    yield random.uniform(0, 10)
