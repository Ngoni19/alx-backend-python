#!/usr/bin/env python3
"""Script -> executes multiple coroutines at the same time with async"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Method: spawns wait_random n times with max_delay
        & returns list of all the delays (in float values)."""
    f_time = [wait_random(max_delay) for _ in range(n)]
    f_time = asyncio.as_completed(f_time)
    lag = [await future for future in f_time]
    return lag
