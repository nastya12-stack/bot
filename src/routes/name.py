from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

router = Router()


def gen_message(name: str) -> str:
    return f"Hello, my friend. Your name is <b>{name}</b>."


@router.message(Command("name"))
async def command_about(message: Message) -> None:
    name = message.from_user.full_name
    await message.answer(gen_message(name))


@router.callback_query(F.data == "name")
async def on_callback(query: CallbackQuery) -> None:
    name = query.from_user.full_name
    await query.message.answer(gen_message(name))
