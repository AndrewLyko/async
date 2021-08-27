import asyncio
import time


async def do_smth():
    print('elo - 1')
    await asyncio.sleep(1)
    print("1")
    await asyncio.sleep(1)
    print("2")
    await asyncio.sleep(1)
    print("3")
    print('elo - 1 end')
    return 'elo'


async def do_smth_1():
    print('elo - 2')
    await asyncio.sleep(1)
    print('elo - 2 end')
    return 'elo 2'


def do_other():
    print('xd')
    return 'xd'


async def main():
    test = await asyncio.gather(do_smth(), do_smth_1())
    return test


if __name__ == '__main__':
    asyncio.run(main())
    print(do_other())