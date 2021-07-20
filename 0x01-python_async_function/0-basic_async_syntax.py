#!/usr/bin/env python3
"""
wait_random
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    generate a random float, sleep then return the random float
    """
    rand = random.uniform(0.0, max_delay)
    await asyncio.sleep(rand)
    return rand
