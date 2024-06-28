from aiogram import Router

from . import about, menu, name, start

router = Router()

router.include_routers(
    about.router,
    start.router,
    menu.router,
    name.router,
)