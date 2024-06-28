from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from routes import menu

router = Router()


@router.message(CommandStart())
async def command_start(message: Message) -> None:
    await menu.show_menu(message)