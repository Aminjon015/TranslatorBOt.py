from data.loader import dp
from aiogram import executor
import handlers

if __name__ == '__main__':
    executor.start_polling(dp)