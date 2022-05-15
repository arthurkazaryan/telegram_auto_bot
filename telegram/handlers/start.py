from aiogram import types
from aiogram.dispatcher import FSMContext, Dispatcher
from telegram.create_bot import bot, dp
from telegram.keyboards.start import keyboard_start
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters.state import State, StatesGroup


# @dp.message_handler(commands=['start', 'help'])
async def commands_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Добро пожаловать на бот по подбору автомобилей!\n'
                                                     'Выберите требуемое действие:', reply_markup=keyboard_start)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС. Напишите ему: @pizzeria_test_bot')


def register_start_handlers(dispatcher: Dispatcher):
    dispatcher.register_message_handler(commands_start, commands=['start', 'help'])
