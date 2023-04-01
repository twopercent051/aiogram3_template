import asyncio

from tgbot.handlers import admin, user, echo
# from tgbot.filters.admin import AdminFilter
# from tgbot.handlers.admin import register_admin
# from tgbot.handlers.user import register_user
# from tgbot.handlers.echo import register_echo
# from tgbot.middlewares.environment import EnvironmentMiddleware
from tgbot.misc.scheduler import scheduler_jobs
from tgbot.models.sql_connector import sql_start
from tgbot.models.redis_connector import redis_start

from create_bot import bot, dp, config, scheduler, logger


# def register_all_middlewares(dp, config):
#     dp.setup_middleware(EnvironmentMiddleware(config=config))


# def register_all_filters(dp):
#     dp.filters_factory.bind(AdminFilter)
#     pass
#
#
# def register_all_handlers(dp):
#     register_admin(dp)
#     register_user(dp)
#     register_echo(dp)


async def main():
    logger.info("Starting bot")

    # bot['config'] = config

    # register_all_middlewares(dp, config)
    # register_all_filters(dp)
    # register_all_handlers(dp)
    scheduler_jobs()
    # await sql_start()
    # redis_start()
    dp.include_routers(admin.router, user.router, echo.router)

    # start
    try:
        scheduler.start()
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await dp.storage.close()
        # await dp.storage.wait_closed()
        await bot.session.close()
        scheduler.shutdown(True)


if __name__ == '__main__':
    try:

        asyncio.run(main())

    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
