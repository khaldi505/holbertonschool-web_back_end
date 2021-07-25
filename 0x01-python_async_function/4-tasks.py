#!/usr/bin/env python3
"""
wait_n
"""
import asyncio
import typing


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    a7dohom lam yanem, ala khater realpython documention
    """
    x = await asyncio.gather(*[task_wait_random(max_delay) for y in range(n)])
    return sorted(x)
