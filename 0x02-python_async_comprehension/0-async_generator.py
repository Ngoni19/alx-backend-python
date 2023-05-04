#!/usr/bin/env python3
"""Script -> Creates a generator"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Method : waits asynchronously for 1 sec each time
    then yields a random floating-point number between 0 and 10"""
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
