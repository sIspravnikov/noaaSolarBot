
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from config_reader import config
from classes.sources import Sources

router = Router()
newline = "\n"

startMessage = f"""
Текущие возможности:
- LASCO CORONAGRAPH
{newline.join(f"/{source}" for source in Sources.sources)}
"""

@router.message(Command("start"))
async def start_cmd(message: Message):
    await message.answer(
        startMessage
    )
