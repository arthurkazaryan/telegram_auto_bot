from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from telegram.create_bot import bot, dp
from telegram.keyboards.start import keyboard_start


class FSMSearchParameters(StatesGroup):
    manufacturer = State()
    model = State()
    # category = State()
    year_from = State()
    year_to = State()
    price_from = State()
    price_to = State()
    # km_age_from = State()
    # km_age_to = State()
    # displacement_from = State()
    # displacement_to = State()
    # transmission = State()
    # gear_type = State()
    # body_type_group = State()
    # engine_group = State()
    # section = State()


async def start_parameters(message: types.Message):
    await FSMSearchParameters.manufacturer.set()
    await message.reply('Напишите название производителя:')


async def select_manufacturer(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['manufacturer'] = message.text
    await FSMSearchParameters.next()
    await message.reply("Напишите название модели:")


async def select_model(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['model'] = message.text
    await FSMSearchParameters.next()
    await message.reply("Напишите год от:")


async def year_from(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['year_from'] = int(message.text)
    await FSMSearchParameters.next()
    await message.reply("Напишите год до:")


async def year_to(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['year_to'] = int(message.text)
    await FSMSearchParameters.next()
    await message.reply("Напишите цену от:")


async def price_from(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price_from'] = int(message.text)
    await FSMSearchParameters.next()
    await message.reply("Напишите цену до:")


async def price_to(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price_to'] = int(message.text)
    async with state.proxy() as data:
        await message.reply(str(data))
        await message.reply(message.chat.id)
    await state.finish()


def register_search_handlers(dispatcher: Dispatcher):
    dispatcher.register_message_handler(start_parameters, commands=['Изменить'], state=None)
    dispatcher.register_message_handler(select_manufacturer, state=FSMSearchParameters.manufacturer)
    dispatcher.register_message_handler(select_model, state=FSMSearchParameters.model)
    dispatcher.register_message_handler(year_from, state=FSMSearchParameters.year_from)
    dispatcher.register_message_handler(year_to, state=FSMSearchParameters.year_to)
    dispatcher.register_message_handler(price_from, state=FSMSearchParameters.price_from)
    dispatcher.register_message_handler(price_to, state=FSMSearchParameters.price_to)
#     dispatcher.register_message_handler(load_photo, content_types=['Photo'], state=FSMAdmin.photo)
#     dispatcher.register_message_handler(load_name, state=FSMAdmin.name)
#     dispatcher.register_message_handler(load_description, state=FSMAdmin.description)
#     dispatcher.register_message_handler(load_price, state=FSMAdmin.price)
#     dispatcher.register_message_handler(make_changes_command, commands=['moderator'], is_chat_admin=True)