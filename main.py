import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config_reader import config
from handlers import start, lascoC2, lascoC3

async def main():
   logging.basicConfig(
      level=logging.INFO,
      format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
   )
   dispatcher = Dispatcher(storage=MemoryStorage())
   bot = Bot(config.bot_token.get_secret_value())

   dispatcher.include_router(start.router)
   dispatcher.include_router(lascoC2.router)
   dispatcher.include_router(lascoC3.router)

   await dispatcher.start_polling(bot)


if __name__ == '__main__':
   asyncio.run(main())