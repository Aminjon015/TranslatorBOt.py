from data.loader import dp
from aiogram import types
from keybords.replay import keyb

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    text = f'''Здравствуйте {message.from_user.full_name}
Я могу переводит слова!'''
    await message.reply(text, reply_markup = keyb)

@dp.message_handler(regexp='Russian Lang 🌐')
async def reaction_to_ru_lang(message: types.Message):
    await message.reply("Напишите что нибудь")
    # await dp.send_message(message.from_user.id, "Напишите что нибудь!")
    # msg = dp.



