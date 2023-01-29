import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

import os

from keyboards import *
from messages import MESSAGES





class UserState(StatesGroup):
    name = State()
    email = State()
    category = State()
    reg = State()
    picture1 = State()
    picture2 = State()

bot = Bot(token = TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(MESSAGES['start'])
    await message.answer(MESSAGES['name'])
    await UserState.name.set()


@dp.message_handler(state=UserState.name)
async def get_username(message: types.Message, state: FSMContext):
    await state.update_data(username=message.text)
    await message.answer(MESSAGES['mail'])
    await UserState.email.set()


@dp.message_handler(state=UserState.email)
async def get_email(message: types.Message, state: FSMContext):
    await state.update_data(username=message.text)
    await message.answer(MESSAGES['user_info'])
    await UserState.category.set()


@dp.message_handler(state=UserState.category)
async def get_cat(message: types.Message, state: FSMContext):
    await state.update_data(username=message.text)
    await message.answer(MESSAGES['success'])
    await message.answer(MESSAGES['begin'])
    await UserState.reg.set()


@dp.message_handler(state=UserState.reg)
async def circle_of_gan(message: types.Message):
    await message.answer(MESSAGES['keyboard'], reply_markup=inline_kb)


@dp.callback_query_handler(state=UserState.reg, text="get_pic_1")
async def get_pictures_process(callback: types.CallbackQuery):
    await callback.message.answer(MESSAGES['send'])
    await callback.answer(MESSAGES['cb_answ'])
    await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
    await UserState.picture1.set()

@dp.callback_query_handler(state=UserState.reg, text="info")
async def get_pictures_process(callback: types.CallbackQuery):
    await callback.message.answer(MESSAGES['info'])


@dp.callback_query_handler(state=UserState.reg, text="info_dev")
async def get_pictures_process(callback: types.CallbackQuery):
    await callback.message.answer(MESSAGES['dev'])


@dp.message_handler(state=UserState.picture1, content_types="photo")
async def get_picture_1(message: types.Message):
    await message.photo[-1].download(destination=f"pictures/{message.from_user.id}_1.jpg", make_dirs=True)
    await message.answer(MESSAGES['pic1'])
    await UserState.picture2.set()


@dp.message_handler(state=UserState.picture2, content_types="photo")
async def get_picture_2(message: types.Message):
    await message.photo[-1].download(destination=f"pictures/{message.from_user.id}_2.jpg", make_dirs=True)
    await message.answer(MESSAGES['pic2'])
    photo = open(f'pictures/{message.from_user.id}_2.jpg', 'rb')
    #there will be transfer
    await message.answer_photo(photo, caption=MESSAGES['result'])
    os.remove(f"pictures/{message.from_user.id}_1.jpg")
    os.remove(f"pictures/{message.from_user.id}_2.jpg")
    await message.answer(MESSAGES['begin'])
    await UserState.reg.set()


#@dp.message_handler()
#async def echo_message(msg: types.Message):
#    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    print('Starting...')
    executor.start_polling(dp)