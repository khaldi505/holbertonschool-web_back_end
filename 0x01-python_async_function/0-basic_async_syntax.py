#!/usr/bin/env python3
import random
import asyncio
"""
wait_random
"""


async def wait_random(max_delay: int=10) -> float:
    """
    generate a random float, sleep then return the random float
    """
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
