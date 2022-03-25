import asyncio


async def function_to_sum_two_values(x, y):
    await asyncio.sleep(1)
    return x + y
