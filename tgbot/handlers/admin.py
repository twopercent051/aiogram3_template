from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import F, Router
from aiogram.filters.state import StateFilter

from tgbot.filters.admin import AdminFilter

router = Router()
router.message.filter(AdminFilter)


@router.message(CommandStart, StateFilter('*'))
async def admin_start(message: Message):
    pass
