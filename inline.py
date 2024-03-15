from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder

class MyCallback(CallbackData, prefix="my"):
    foo: str
    bar: int

def create_markup():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Yanvar",
        callback_data=MyCallback(foo="yanvar", bar="42")  # Value can be not packed to string inplace, because builder knows what to do with callback instance
    )

    builder.button(
        text="Fevral",
        callback_data=MyCallback(foo="fevral", bar="43")  # Value can be not packed to string inplace, because builder knows what to do with callback instance
    )

    builder.button(
        text="Mart",
        callback_data=MyCallback(foo="mart", bar="43")  # Value can be not packed to string inplace, because builder knows what to do with callback instance
    )

    builder.button(
        text="April",
        callback_data=MyCallback(foo="april", bar="43")  # Value can be not packed to string inplace, because builder knows what to do with callback instance
    )

    builder.button(
        text="May",
        callback_data=MyCallback(foo="may", bar="43")  # Value can be not packed to string inplace, because builder knows what to do with callback instance
    )

    builder.button(
        text="Iyun",
        callback_data=MyCallback(foo="iyun", bar="43")  # Value can be not packed to string inplace, because builder knows what to do with callback instance
    )

    builder.button(
        text="Iyul",
        callback_data=MyCallback(foo="iyul", bar="43")  # Value can be not packed to string inplace, because builder knows what to do with callback instance
    )

    builder.button(
        text="Avgust",
        callback_data=MyCallback(foo="avgust", bar="43")  # Value can be not packed to string inplace, because builder knows what to do with callback instance
    )

    builder.button(
        text="Sentyabr",
        callback_data=MyCallback(foo="sentyabr", bar="43")  # Value can be not packed to string inplace, because builder knows what to do with callback instance
    )

    builder.button(
        text="Oktyabr",
        callback_data=MyCallback(foo="oktyabr", bar="43")  # Value can be not packed to string inplace, because builder knows what to do with callback instance
    )

    builder.button(
        text="Noyabr",
        callback_data=MyCallback(foo="noyabr", bar="43")  # Value can be not packed to string inplace, because builder knows what to do with callback instance
    )

    builder.button(
        text="Dekabr",
        callback_data=MyCallback(foo="dekabr", bar="43")  # Value can be not packed to string inplace, because builder knows what to do with callback instance
    )
    
    builder.adjust(2, )

    return builder.as_markup()


# async def subcategories_keyboard(subcategories):
    # markup = InlineKeyboardMarkup(row_width=1)

    # for i in subcategories:
    #     button_text = i[1]

    #     callback_data = sub_category_callback.new(category=i[2], id=i[0] )
        
        
    #     markup.insert(
    #         InlineKeyboardButton(text=button_text, callback_data=callback_data)
    #     )

    # markup.row(
    #     InlineKeyboardButton(
    #         text="⬅️Ortga", callback_data=back_callback.new(category_id=0, subcategory_id=0))
    #     )
    # return markup

# https://docs.aiogram.dev/en/latest/utils/keyboard.html
# https://github.com/Abdurasuloff/web_store_bot/blob/main/bot/keyboards/inline/products_buttons.py
# https://github.com/MasterGroosha/telegram-feedback-bot/blob/master/bot/handlers/adminmode.py



# https://github.com/PythonHubStudio/aiogram-3-course-telegram-bot/blob/main/lesson_8_multi_level_inline_menu/handlers/admin_private.py