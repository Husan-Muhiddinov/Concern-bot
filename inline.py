from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData

class MyCallback(CallbackData, prefix="my"):
    foo: str
    bar: int

def create_markup():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="demo",
        callback_data=MyCallback(foo="demo", bar="42")  # Value can be not packed to string inplace, because builder knows what to do with callback instance
    )



# https://docs.aiogram.dev/en/latest/utils/keyboard.html
# https://github.com/Abdurasuloff/web_store_bot/blob/main/bot/keyboards/inline/products_buttons.py
# https://github.com/MasterGroosha/telegram-feedback-bot/blob/master/bot/handlers/adminmode.py