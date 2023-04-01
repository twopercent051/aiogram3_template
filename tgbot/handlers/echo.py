from aiogram import types, Dispatcher
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram import F, Router

router = Router()


@router.message(Command('get_id'))
async def get_id(message: types.Message):
    print(111)
    chat_id = message.chat.id
    user_id = message.from_user.id
    text = f'user_id: {user_id} || chat_id: {chat_id}'
    print(text)
    await message.answer(text)

