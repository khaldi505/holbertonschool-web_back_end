#!/usr/bin/env python3
'''
OFC
'''
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    YES
    '''
    before_e = time.perf_counter()
    e = await asyncio.gather(*(async_comprehension() for i in range(4)))
    after_e = time.perf_counter() - before_e
    return after_e
