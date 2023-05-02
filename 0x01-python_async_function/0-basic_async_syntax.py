#!/usr/bin/env python3
"""Scipt -> Defines an asynchronous coroutine"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random delay between 0 and max_delay"""
    random_number = random.uniform(0, max_delay)
    await asyncio.sleep(random_number)
    return random_number
 
def random_delay(max_delay: int) -> Callable[[], float]:
    """Returns a function that generates a random delay"""
    return (lambda : random.uniform(0, max_delay))
 
async def wait_random_optimized(max_delay: int = 10) -> float:
    """Waits for a random delay between 0 and max_delay"""
    rand_func = random_delay(max_delay)
    random_number = rand_func()
    await asyncio.sleep(random_number)
    return random_number

