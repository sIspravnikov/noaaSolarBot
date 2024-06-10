import os
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from classes.render import Render
from aiogram.types import FSInputFile

router = Router()
animationType = "lasco_c3"
source = 'https://services.swpc.noaa.gov/images/animations/lasco-c3/'
framesExtension = 'jpg'

paths = {
    'frames': f"{os.path.join(os.getcwd(),'data',animationType, 'frames')}",
    'gif': f"{os.path.join(os.getcwd(),'data',animationType, 'gif')}",
    'video': f"{os.path.join(os.getcwd(),'data',animationType, 'mp4')}"
}

outputgif = f"{os.path.join(paths['gif'], animationType)}.gif"
outputvideo = f"{os.path.join(paths['video'], animationType)}.mp4"

# кадров в секунду для видео
fps=15

@router.message(Command(commands=[f"{animationType}"]))
async def cmd_lasco_c2(message: Message):
    await message.answer(
        text="Запрос обрабатывается",
        reply_markup=ReplyKeyboardRemove()
    )
    render = Render(paths)
    render.mp4(outputvideo, fps)

    await message.answer_video(
        video = FSInputFile(outputvideo),
        reply_markup=ReplyKeyboardRemove()
    )