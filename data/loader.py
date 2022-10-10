from aiogram import Bot, Dispatcher
import os
from dotenv import load_dotenv
from googletrans import Translator

load_dotenv()

TOKEN = os.getenv('TOKEN')

bot = Bot(TOKEN)
dp = Dispatcher(bot)
translator = Translator()