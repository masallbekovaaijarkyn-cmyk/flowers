from aiogram import Bot, Dispatcher, F, Router
import asyncio
from dotenv import load_dotenv
import os
load_dotenv()
TOKEN = os.getenv("TOKEN")
# print(TOKEN)
bot = Bot(token=TOKEN)
dp = Dispatcher()
async def start_up():
    print("-------------I woke up BOSS-------------")
async def off():
    print("-----------I sleep BOSS------------")
async def main():
    dp.startup.register(start_up)
    dp.shutdown.register(off)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())