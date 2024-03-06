import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from buttons import menu
from aiogram.filters import Command
from aiogram import Router, F, Bot

# Bot token can be obtained via https://t.me/BotFather
TOKEN = str("7195481777:AAH2wTRKtoWxQ5Fos84kw75eLjCy31JoBno")

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!", reply_markup=menu)


# @router.message(F.text == 'hello')
# @router.inline_query(F.data == 'button:1')
# @router.message(F.text.startswith('foo'))
# @router.message(F.content_type.in_({'text', 'sticker'}))
# @router.message(F.text.regexp(r'\d+'))


@dp.message(F.text == "✈️ Umra sayohatlari")
async def show_category(message: types.Message):
    await message.answer(f"Hello")



# @dp.message()
# async def echo_handler(message: types.Message) -> None:

#     try:
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         await message.answer("Nice try!")


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())