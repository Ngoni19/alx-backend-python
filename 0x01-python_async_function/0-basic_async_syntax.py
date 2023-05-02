#!/usr/bin/env python3
"""Script -> Defines an asynchronous coroutine"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Method: Waits for a random delay between 0 & max_delay"""
    rand_num = random.uniform(0, max_delay)
    await asyncio.sleep(rand_num)
    return rand_num
