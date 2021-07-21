import asyncio
import time


def sleep_for_seconds(n):
    print(f'Starting sleep for {n} seconds')
    time.sleep(n)  # time.sleep is a blocking call
    print(f'Done sleep for {n} seconds')


# # Synchronous execution
#
# sleep_for_seconds(1)
# sleep_for_seconds(2)
# sleep_for_seconds(3)



async def asynchronous_sleep_for_seconds(n):
    print(f'Starting sleep for {n} seconds')
    await asyncio.sleep(n)  # asyncio.sleep is a non blocking call
    print(f'Done sleep for {n} seconds')


# Asynchronous execution

async def main():
    await asyncio.gather(
        asynchronous_sleep_for_seconds(1),
        asynchronous_sleep_for_seconds(2),
        asynchronous_sleep_for_seconds(3),
)

asyncio.run(main())
