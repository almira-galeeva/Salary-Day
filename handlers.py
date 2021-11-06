from main import bot, dp

from aiogram.types import Message
from config import admin_id
from salary_class import SalaryDay

async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text='Bot is running')
    
@dp.message_handler()
async def how_many_days_left(message: Message):
    sd = SalaryDay()
    sd.res_phrase()
    print(sd.variants)
   
    await message.answer(text=sd.word_days)