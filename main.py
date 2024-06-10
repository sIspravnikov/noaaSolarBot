import os
import asyncio
import logging
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config_reader import config
from handlers import start, lascoC2, lascoC3
from classes.noaa import NOAA

async def getFiles():
   paths = {
    'frames': 'frames',
    'gif': 'gif',
    'video': 'mp4'
   }

   sources = {
      'lascoC2': {
         'extension': 'jpg', 
         'url': 'https://services.swpc.noaa.gov/images/animations/lasco-c2/',
      },
      'lascoC3': {
         'extension': 'jpg', 
         'url': 'https://services.swpc.noaa.gov/images/animations/lasco-c3/',
      }
   }
   for source, params in sources.items():
      noaa = NOAA(source, params['url'], params['extension'], paths)
      await noaa.getFiles()

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

   scheduler = AsyncIOScheduler()
   scheduler.add_job(getFiles, 'interval', seconds=60)
   # scheduler.add_job(cleanFiles, 'interval', seconds = 60)
   scheduler.start()

   await dispatcher.start_polling(bot)


if __name__ == '__main__':
   asyncio.run(main())