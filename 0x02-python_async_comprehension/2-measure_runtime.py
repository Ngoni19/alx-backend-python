#!/usr/bin/env python3
"""Script->Measures runtime of async_comprehension 
    executed 4 times in parallel"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Executes async_comprehension 4 times in parallel
        & measure_runtime should measure the total runtime & return it"""
    s_time = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    return time.perf_counter() - s_time
