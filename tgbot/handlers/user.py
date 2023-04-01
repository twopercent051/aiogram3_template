from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import F, Router
from aiogram.fsm.context import FSMContext

router = Router()


@router.message(CommandStart)
async def user_start(message: Message):
    pass


@router.message(F.text)
async def user_start(message: Message):
    await message.answer(message.text)
