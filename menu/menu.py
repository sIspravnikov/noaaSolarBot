from aiogram import Bot
from aiogram.types import BotCommand
from classes.sources import Sources

async def set_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(
            command=f"/{source}",
            description=params['description']
        ) for source, params in Sources.sources.items()
    ]
    await bot.set_my_commands(main_menu_commands)