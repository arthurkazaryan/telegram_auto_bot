from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_settings = KeyboardButton('/Параметры')
button_change_settings = KeyboardButton('/Изменить')

keyboard_start = ReplyKeyboardMarkup(resize_keyboard=True)  # one_time_keyboard=True
keyboard_start.row(button_settings, button_change_settings)  # .row(b4, b5)
