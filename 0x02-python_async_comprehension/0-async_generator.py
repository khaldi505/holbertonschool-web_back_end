#!/usr/bin/env python3
"""
async_generator module
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    async_generator
    """
    for x in range(10):
        await asyncio.sleep(1)
        yield(random.uniform(0, 10))
