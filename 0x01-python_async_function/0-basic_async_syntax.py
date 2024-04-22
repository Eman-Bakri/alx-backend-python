#!/usr/bin/env python3
"""
    max delay and wait random
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """using wait_random"""
    random_delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
