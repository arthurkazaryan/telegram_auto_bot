from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from telegram.api_key import api_key

storage = MemoryStorage()

bot = Bot(token=api_key)
dp = Dispatcher(bot, storage=storage)
