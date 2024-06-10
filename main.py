import asyncio
import logging
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config_reader import config
from handlers import start, lasco_c3, lasco_c2, enlil, sdo_hmii
from handlers.menu import set_menu
from classes.noaa import NOAA
from classes.sources import Sources

async def cleanFiles():
   pass

async def getFiles():
   paths = {
    'frames': 'frames',
    'gif': 'gif',
    'video': 'mp4'
   }

   for source, params in Sources.sources.items():
      noaa = NOAA(source, params['url'], params['extension'], paths)
      await noaa.getFiles()

async def main():
   logging.basicConfig(
      level=logging.INFO,
      format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
   )
   dispatcher = Dispatcher(storage=MemoryStorage())
   bot = Bot(config.bot_token.get_secret_value())

   await set_menu(bot)

   dispatcher.include_router(start.router)
   dispatcher.include_router(lasco_c2.router)
   dispatcher.include_router(lasco_c3.router)
   dispatcher.include_router(enlil.router)
   dispatcher.include_router(sdo_hmii.router)

   scheduler = AsyncIOScheduler()
   scheduler.add_job(getFiles, 'interval', seconds=600)
   # scheduler.add_job(cleanFiles, 'interval', seconds = 700)
   scheduler.start()

   await dispatcher.start_polling(bot)


if __name__ == '__main__':
   asyncio.run(main())