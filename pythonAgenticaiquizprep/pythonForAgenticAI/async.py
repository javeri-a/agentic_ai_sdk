import asyncio

async def chai_banao():
    print("☕ Chai ban rahi hai...")
    await asyncio.sleep(3)   # 3 second rukenge
    print("✅ Chai tayyar!")

async def paratha_banao():
    print("🍳 Paratha ban raha hai...")
    await asyncio.sleep(2)   # 2 second rukenge
    print("✅ Paratha tayyar!")

async def main():
    await asyncio.gather(
        chai_banao(),
        paratha_banao()
    )

asyncio.run(main())

async def paratha_banao():
    print("🍳 Paratha ban raha hai...")
    await asyncio.sleep(2)   # 2 second rukenge
    print("✅ Paratha tayyar!")

async def main():
    await asyncio.gather(
        chai_banao(),
        paratha_banao()
    )

asyncio.run(main())



async def main():
    await asyncio.gather(
        chai_banao(),
        paratha_banao()
    )

asyncio.run(main())


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(4))  # Output: True
print(is_even(7))