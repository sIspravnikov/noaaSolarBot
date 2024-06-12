
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from classes.sources import Sources
from classes.messages import Messages
from aiogram.utils.formatting import as_list, Bold

router = Router()
newline = "\n"

startMessage = as_list(f"{Messages.release_notes}")

@router.message(Command("release_notes"))
async def cmd_rn(message: Message):
    await message.answer(
        **startMessage.as_kwargs()
    )
