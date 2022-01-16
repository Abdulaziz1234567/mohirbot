import logging
 
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5027977030:AAHRsLEr9E02afeP-MPoYtg8DK7IugAJkPs'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
   """
   This handler will be called when user sends `/start` or `/help` command
    """
   await message.reply("«««««««««« Assalom Alekum »»»»»»»»»»\n💻 Abdulaziz_dev bo'tiga xush kelibsiz 💻\n portfolio: http://a90370s1.beget.tech/index.html")


@dp.message_handler()
async def echo(message: types.Message):
   # old style:
   # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
   
