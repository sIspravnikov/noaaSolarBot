import os
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from classes.render import Render
from aiogram.types import FSInputFile
from classes.sources import Sources
from classes.messages import Messages

router = Router()
animationType = os.path.basename(__file__).split('.')[0]
source = Sources.sources[animationType]['url']
framesExtension = Sources.sources[animationType]['extension']

default_frames = 241

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
async def cmd_geospace_ovation(message: Message):
    render = Render(paths, default_frames)
    status = await render.mp4(outputvideo, fps)
    if status:
        await message.reply_video(
            video = FSInputFile(outputvideo),
            reply_markup=ReplyKeyboardRemove()
        )
    else:
        await message.reply(
            text=Messages.error
        )
    await render.remove(outputvideo)