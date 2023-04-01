import asyncio
from aiogram import Bot, Dispatcher
from tgbot.handlers import admin, echo, user


# Запуск бота
async def main():
    bot = Bot(token="5921117513:AAGbrJQA5qVqysf3OxR-1j8nF-QE9LzJWq0")
    dp = Dispatcher()

    dp.include_routers(admin.router, echo.router, user.router)

    # Альтернативный вариант регистрации роутеров по одному на строку
    # dp.include_router(questions.router)
    # dp.include_router(different_types.router)

    # Запускаем бота и пропускаем все накопленные входящие
    # Да, этот метод можно вызвать даже если у вас поллинг
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())