#!/usr/bin/env python3
"""Script -> execute multiple coroutines at the same time with async"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Method: spawns wait_random n times with max_delay
        & returns list of all the delays in float values"""
    f_time = [task_wait_random(max_delay) for _ in range(n)]
    f_time = asyncio.as_completed(f_time)
    lag_time = [await future for future in f_time]
    return lag_time
