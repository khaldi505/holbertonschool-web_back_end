#!/usr/bin/env python3
import random
import asyncio

async def wait_random(max_delay: float=10):
    rand = random.uniform(0.0, float(max_delay))
    await asyncio.sleep(rand)
    return rand
