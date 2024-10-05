import os
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from classes.render import Render
from aiogram.types import FSInputFile
from classes.sources import Sources
from classes.messages import Messages
from classes.storage import Storage
from classes.debug import Debug

router = Router()
routerName = os.path.basename(__file__).split('.')[0]
source = Sources.sources[routerName]['url']
framesExtension = Sources.sources[routerName]['dataType']

default_frames = 42

paths = {
    'frames': f"{os.path.join(Storage.basepath,routerName, 'frames')}",
    'gif': f"{os.path.join(Storage.basepath,routerName, 'gif')}",
    'video': f"{os.path.join(Storage.basepath,routerName, 'mp4')}"
}

outputgif = f"{os.path.join(paths['gif'], routerName)}.gif"
outputvideo = f"{os.path.join(paths['video'], routerName)}.mp4"

# кадров в секунду для видео
fps=15

@router.message(Command(commands=[f"{routerName}"]))
async def cmd_suvi_131(message: Message):
    Debug.print_user(message)
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