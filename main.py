import asyncio
from sys import prefix

from aiogram import  Bot, Dispatcher, types
from  aiogram.filters.command import Command, CommandObject
from api_token import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher()

TEXT = '''
/help - справочний текст
/start - запуск бота
'''

@dp.message(Command('start'))
async def start_command(message: types.Message):
    await message.answer('Привет,я бот!')


@dp.message(Command('help'))
async def help_command(message: types.Message):
    await message.reply(TEXT)

@dp.message(Command('test_args'))
async def test_args_command(message: types.Message, command: CommandObject):
    await message.answer(command.args)

async def main():
    await bot.delete_webhook(drop_pending_updates=True) #проигнорировать апдейты бота
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
