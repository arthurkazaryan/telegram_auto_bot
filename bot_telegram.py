from aiogram.utils import executor
from telegram.create_bot import dp
from telegram.handlers import start, search_parameters
from database.utils import start_database
from pathlib import Path


async def on_startup(_):
    print('Запуск бота')
    # start_database(Path.cwd().joinpath('database', 'users.db'))

start.register_start_handlers(dp)
search_parameters.register_search_handlers(dp)
# other.register_handlers_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)  # True - Когда бот был оффлайн сообщения скипаются
