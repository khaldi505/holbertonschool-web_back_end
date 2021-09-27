#!/usr/bin/env python3
"""
async_Comprehensions module
"""
import asyncio
from typing import Generator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """
    """
    random_number = [number async for number in async_generator()]
    return random_number
