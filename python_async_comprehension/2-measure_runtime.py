#!/usr/bin/env python3
"""
Write a measure_runtime function that executes async_comprehension four times
in parallel using asyncio.gather, and returns the total runtime.
"""

import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the runtime of executing async_comprehension
    four times in parallel."""
    start_time = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end_time = time.time()
    total_time = end_time - start_time
    return total_time
