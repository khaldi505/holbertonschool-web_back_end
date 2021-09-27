#!/usr/bin/env python3
"""
async_generator module
"""
import asyncio
import random


async def async_generator() -> None:
    """
    async_generator
    """
    for x in range(10):
        await asyncio.sleep(1)
        yield(random.uniform(0, 10))
