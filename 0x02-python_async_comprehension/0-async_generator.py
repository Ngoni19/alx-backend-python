#!/usr/bin/env python3

"""Script -> Asynchronously generates random numbers"""

import asyncio
import random
from typing import AsyncGenerator


async def generate_random_numbers() -> AsyncGenerator[float, None]:
    """Method: Waits asynchronously for 1 sec each time,
    then yields a random floating-point number between 0 & 10"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

