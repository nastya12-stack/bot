from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

router = Router()


@router.message(Command("about"))
async def command_about(message: Message) -> None:
    await message.answer("This bot was created @Настя Хохлова.")


@router.callback_query(F.data == "about")
async def on_callback(query: CallbackQuery) -> None:
    await query.message.answer("This bot was created @Настя Хохлова.")