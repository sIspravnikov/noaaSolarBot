import os
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from classes.noaa import NOAA
from classes.render import Render
from aiogram.types import FSInputFile

router = Router()
animationType = "lascoC3"
source = 'https://services.swpc.noaa.gov/images/animations/lasco-c3/'
framesExtension = 'jpg'

paths = {
    'frames': f"{animationType}frames",
    'gif': f"{animationType}gif",
    'video': f"{animationType}mp4"
}

outputgif = f"{os.path.join(paths['gif'], animationType)}.gif"
outputvideo = f"{os.path.join(paths['video'], animationType)}.mp4"

# кадров в секунду для видео
fps=15

@router.message(Command(commands=[f"{animationType}"]))
async def cmd_lascoC3(message: Message):
    if (message.from_user.id == 217513939):
        await message.answer(
            text="Запрос обрабатывается",
            reply_markup=ReplyKeyboardRemove()
        )

        noaa = NOAA(source, framesExtension, paths)
        noaa.getFiles()

        render = Render(paths)
        render.gif(outputgif)
        render.mp4(outputvideo, fps)

        await message.answer_video(
            video = FSInputFile(outputvideo),
            reply_markup=ReplyKeyboardRemove()
        )
    else:
        await message.answer(
            text=f"Бот пока кривоват и отвечает только одному кожаному ублюдку - хозяину",
            reply_markup=ReplyKeyboardRemove()
        )