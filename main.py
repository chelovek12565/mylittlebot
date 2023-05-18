from aiogram import Bot, Dispatcher, executor, types
from random import randint, random
import asyncio
import aioschedule
from pip._internal import commands

with open("somedata", "rt") as f:
    API_TOKEN = f.read()

PROXY_URL = "http://proxy.server:3128/"

STICKER_IDS = [
    "CAACAgIAAxkBAAEJBXFkZhz09YJOQn3UJGpQke3bQd46jwACMAADXHekE9-2xp6URB8vLwQ",
    "CAACAgIAAxkBAAEJBXNkZhz3xgcDpQxI6vmN-VRdCvYxLgACRAADXHekE28I3fKw17hfLwQ",
    "CAACAgIAAxkBAAEJBXVkZhz-jtn9DKRu6LmQ6n2Y6gYAAXUAAkUAA1x3pBPM1OHF_G551y8E",
    "CAACAgIAAxkBAAEJBXdkZh0AAdk24jaMya6Gqp7Y1m1VlC0AAkYAA1x3pBMRsMYRJ0n12S8E",
    "CAACAgIAAxkBAAEJBXlkZh0F7sPWoOqftS1DM2cGvXHv2AACRwADXHekE4bDwVuDj4DNLwQ",
    "CAACAgIAAxkBAAEJBXtkZh0OsVS6EZ98CLBkYr3e8E0sNQACLQADXHekE9jDc5aYErAXLwQ",
    "CAACAgIAAxkBAAEJBX1kZh0TLzdfi09IQMqKtY8pUdDkwAACfwADXHekE73D84sHd3iyLwQ",
    "CAACAgIAAxkBAAEJBX9kZh0WZ4CQCzN1cLU4ZnW_ttyIlAACaAADXHekE-PiKmvJfmwTLwQ",
    "CAACAgIAAxkBAAEJBYFkZh0aec2485LH0CIc_DySzjOkfAACaQADXHekEyV88c945fViLwQ",
    "CAACAgIAAxkBAAEJBYNkZh0e3o74eLujkRbSJeBWe0Af4gACagADXHekE84s-QzL5mjfLwQ",
    "CAACAgIAAxkBAAEJBYVkZh0iZ4adsMBQbsgUUvNeAAG_zxgAAmsAA1x3pBOKWc8aKR8bqC8E",
    "CAACAgIAAxkBAAEJBYdkZh0m4rjFaK4o8COCriNCyM6wuwACbAADXHekE_S8TtViKR8zLwQ",
    "CAACAgIAAxkBAAEJBYlkZh0qAtQjHDBSFyS67ZMe7_6bkAACbQADXHekEyY7VNCszeszLwQ",
    "CAACAgIAAxkBAAEJBYtkZh0u_9XD6sQzkgABvfEVQLUBQcoAAm4AA1x3pBMTT_R4CjUp-y8E",
    "CAACAgIAAxkBAAEJBY1kZh0ygVjUMkiujLUICCjYKu86agACbwADXHekE3vMkZZ1E-HmLwQ",
    "CAACAgIAAxkBAAEJBY9kZh04YOugFsOuE01hOZBdOjQ2JwACcwADXHekE7iVxMjzhFW7LwQ",
    "CAACAgIAAxkBAAEJBZFkZh088K5E-zl7FV4mc_uuzfRkpQACNwADXHekEzxcWgfzcBG-LwQ",
    "CAACAgIAAxkBAAEJBZNkZh1AfaRKMC6d5h8kSBwH5PL-rgACJQADXHekE_D_m5Xtku6ZLwQ",
    "CAACAgIAAxkBAAEJBZVkZh1EL_d2ZazreNqmw0LbZsuDXQACJAADXHekE4wxI9NDzrIPLwQ"
]


reminder_id = None
# bot = Bot(token=API_TOKEN, proxy=PROXY_URL)
bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Я буду творить разную хуйню но в данном случае напоминать ичиго посмотреть сука акудама драйв")


async def remind():
    await bot.send_message(reminder_id, "@Ichigo654 еблан посмотри акудама драйв", disable_notification=True)


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


@dp.message_handler()
async def replier(message: types.Message):
    if random() <= 0.11:
        await message.reply_sticker(sticker=STICKER_IDS[randint(0, len(STICKER_IDS) - 1)])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)