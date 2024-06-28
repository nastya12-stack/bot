from aiogram import Router
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

router = Router()


@router.message(Command("menu"))
async def show_menu(message: Message) -> None:
    keyboard = [
        [InlineKeyboardButton(text="Who created you?", callback_data="about")],
        [InlineKeyboardButton(text="What is my name?", callback_data="name")],
    ]

    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)

    await message.answer("Ask me any of these questions!", reply_markup=markup)