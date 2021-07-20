#!/usr/bin/env python3
import random
import asyncio

"""
wait_random
"""


async def wait_random(max_delay: float=10):
    """
    generate a random float, sleep then return the random float
    """
    rand = random.uniform(0.0, float(max_delay))
    await asyncio.sleep(rand)
    return rand
