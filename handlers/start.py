
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from config_reader import config

router = Router()
newline = "\n"
types = {
    'lascoC2': 'lascoC2',
    'lascoC3': 'lascoC3',
    # 'suvi094': 'suvi094',
    # 'suvi131': 'suvi131',
    # 'suvi171': 'suvi171',
    # 'suvi195': 'suvi195',
    # 'suvi284': 'suvi284',
    # 'suvi304': 'suvi304',
    }

startMessage = f"""
Текущие возможности:
- LASCO CORONAGRAPH
{newline.join(f"/{value}" for value in types)}
"""

@router.message(Command("start"))
async def start_cmd(message: Message):
    await message.answer(
        startMessage
    )
