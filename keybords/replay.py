from aiogram.types import ReplyKeyboardMarkup,\
    KeyboardButton,ReplyKeyboardRemove,\
    InlineKeyboardButton,InlineKeyboardMarkup
import data.config as cfg
keyb = InlineKeyboardMarkup()

for i, j in cfg.LANGDIC.items():
    key = InlineKeyboardButton(j, callback_data=i)
    key.add(key)

# def generate_translator_button():
#     btn1 = KeyboardButton('Russian Lang 🌐')
#     btn2 = KeyboardButton('English Lang 🌐')
#     btn3 = KeyboardButton('French Lang 🌐')
#     btn4 = KeyboardButton('Uzbek Lang 🌐')
#     btn5 = KeyboardButton('Japan Lang 🌐')
#     btn6 = KeyboardButton('Polish Lang 🌐')
#
#     markup_big = ReplyKeyboardMarkup(resize_keyboard=True)
#     markup_big.add(btn1, btn2, btn3, btn4, btn5, btn6)
#     return markup_big
