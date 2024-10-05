import os
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from classes.sources import Sources
from classes.messages import Messages
from classes.text import Text
from classes.debug import Debug

router = Router()
routerName = os.path.basename(__file__).split('.')[0]
source = Sources.sources[routerName]['url']
translator="yandex"

@router.message(Command(commands=[f"{routerName}"]))
async def cmd_discussion(message: Message):
    Debug.print_user(message)
    text = Text(source, translator)
    discussion = text.getText()
    await message.reply(
        text=f"{discussion}"
    )