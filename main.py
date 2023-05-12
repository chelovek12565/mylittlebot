from aiogram import Bot, Dispatcher, executor, types
import asyncio
import aioschedule
from pip._internal import commands

with open("somedata", "rt") as f:
    API_TOKEN = f.read()

reminder_id = None
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Я буду творить разную хуйню но в данном случае напоминать ичиго посмотреть сука акудама драйв")


async def remind():
    await bot.send_message(reminder_id, "@Ichigo654 еблан посмотри акудама драйв")


@dp.message_handler(commands=["remind"])
async def reminder(message: types.Message):
    await remind()


async def scheduler():
    aioschedule.every(1).hour.do(remind)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


@dp.message_handler(commands=["start_reminder"])
async def start_reminder(message: types.Message):
    global reminder_id
    if not reminder_id:
        reminder_id = message.chat.id
        asyncio.create_task(scheduler())



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)