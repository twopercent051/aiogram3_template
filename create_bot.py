import logging
import redis

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from tgbot.config import load_config

config = load_config(".env")
r = redis.Redis(host=config.rds.host, port=config.rds.port, db=config.rds.db)
storage = RedisStorage(redis=r) if config.tg_bot.use_redis else MemoryStorage()
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
dp = Dispatcher()
scheduler = AsyncIOScheduler()

logger = logging.getLogger(__name__)
file_log = logging.FileHandler("logger.log")
console_out = logging.StreamHandler()
logging.basicConfig(handlers=(file_log, console_out), level=logging.INFO)
