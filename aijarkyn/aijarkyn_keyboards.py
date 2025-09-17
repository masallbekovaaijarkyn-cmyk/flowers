from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="/team", callback_data="team")],
    ],

)
menuu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="МЕНЮ", callback_data="menuu")]
    ]
)
