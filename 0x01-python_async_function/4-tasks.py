#!/usr/bin/env python3
"""
Let's execute multiple coroutines at the same time with async
"""
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """task_wait_n: spawn task_wait_random n times with the specified max_delay."""

    delays = []

    for _ in range(n):
        delays.append(await task_wait_random(max_delay))
    return sorted(delays)
