import aioschedule
from asyncio import sleep
from .send_deadlines import send_deadlines


async def setup():
    print("test")
    aioschedule.every().minutes.do(send_deadlines)

    while True:
        await aioschedule.run_pending()
        await sleep(1)


