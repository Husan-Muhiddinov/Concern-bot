from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder
import paginator
# from telegram_bot_pagination import InlineKeyboardPaginator

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







def pages(Paginator: paginator):
    btns = dict()
    if Paginator.has_previous():
        btns["◀ Пред."] = "previous"

    if paginator.has_next():
        btns["След. ▶"] = "next"

    return btns


async def products(session, level, category, page):
    req=requests.get("http://45.137.148.241/facilities/")
    js_req=json.loads(req.text)
    products=list(filter(lambda x: x['month']=="fevral", js_req))
    # products = await orm_get_products(session, category_id=category)

    Paginator = paginator(products, page=page)
    product = paginator.get_page()[0]

    image = InputMediaPhoto(
        media=product.image,
        caption=f"<strong>{product.name}\
                </strong>\n{product.description}\nСтоимость: {round(product.price, 2)}\n\
                <strong>Товар {paginator.page} из {paginator.pages}</strong>",
    )

    pagination_btns = pages(paginator)

    kbds = get_products_btns(
        level=level,
        category=category,
        page=page,
        pagination_btns=pagination_btns,
        product_id=product.id,
    )

    return image, kbds




class MenuCallBack(CallbackData, prefix="menu"):
    level: int
    menu_name: str
    category: int | None = None
    page: int = 1
    product_id: int | None = None


def get_products_btns(
    *,
    level: int,
    category: int,
    page: int,
    pagination_btns: dict,
    product_id: int,
    sizes: tuple[int] = (2, 1)
):
    keyboard = InlineKeyboardBuilder()

    keyboard.add(InlineKeyboardButton(text='Назад',
                callback_data=MenuCallBack(level=level-1, menu_name='catalog').pack()))
    keyboard.add(InlineKeyboardButton(text='Корзина 🛒',
                callback_data=MenuCallBack(level=3, menu_name='cart').pack()))
    keyboard.add(InlineKeyboardButton(text='Купить 💵',
                callback_data=MenuCallBack(level=level, menu_name='add_to_cart', product_id=product_id).pack()))

    keyboard.adjust(*sizes)

    row = []
    for text, menu_name in pagination_btns.items():
        if menu_name == "next":
            row.append(InlineKeyboardButton(text=text,
                    callback_data=MenuCallBack(
                        level=level,
                        menu_name=menu_name,
                        category=category,
                        page=page + 1).pack()))
        
        elif menu_name == "previous":
            row.append(InlineKeyboardButton(text=text,
                    callback_data=MenuCallBack(
                        level=level,
                        menu_name=menu_name,
                        category=category,
                        page=page - 1).pack()))

    return keyboard.row(*row).as_markup()



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