#!/usr/bin/env python3
"""Script -> measures the total execution time for wait_n"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Method: Returns total_time(ie. total exc time / n"""
    s_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    e_time = time.perf_counter()
    return (e_time - s_time) / n
