from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main = InlineKeyboardMarkup(
    inline_keyboard=[

        [InlineKeyboardButton(text="/about", callback_data="about")],
        [InlineKeyboardButton(text="/help", callback_data="help")]

    ]
)
