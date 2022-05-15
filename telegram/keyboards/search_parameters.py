from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_settings = KeyboardButton('/Параметры')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)  # one_time_keyboard=True
# kb_client.add(b1).add(b2).insert(b3)
kb_client.add(button_settings)  # .row(b4, b5)
