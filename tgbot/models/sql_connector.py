import aiomysql
import asyncio
import contextvars

from create_bot import config, logger

connection = contextvars.ContextVar('connection')


async def connection_init():
    host = config.db.host
    user = config.db.user
    password = config.db.password
    db_name = config.db.database
    logger.info('Try connect')
    connection.set(await aiomysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        db=db_name,
        cursorclass=aiomysql.cursors.DictCursor
    ))
    logger.info('connected')
    return connection.get()


async def sql_start():
    await connection_init()
    async with connection.get().cursor() as cursor:
        logger.info('In cursor')
        await cursor.execute("""
            
            """)
        await cursor.execute("""
            
            """)
        logger.info('MySQL connected OK')
        await connection.get().commit()


async def get_users_sql():
    query = ';'
    async with connection.get().cursor() as cursor:
        await cursor.execute(query)
        result = await cursor.fetchall()
    return result
