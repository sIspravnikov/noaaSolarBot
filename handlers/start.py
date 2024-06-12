
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from classes.sources import Sources
from aiogram.utils.formatting import as_list

router = Router()
newline = "\n"

startMessage = as_list(f"""
Текущие возможности:
{newline.join(f"/{source} {params['description']}" for source, params in Sources.sources.items())}

Пока что рендерится такое же количество кадров, как на сайте NOAA. 
Архивные данные скачиваются в фоне и в будущем будет возможность получать и за период
""")

@router.message(Command("start"))
async def start_cmd(message: Message):
    await message.answer(
        **startMessage.as_kwargs()
    )
