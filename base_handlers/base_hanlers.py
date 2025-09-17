from aiogram import Router, F
from aiogram.types import Message

from base_kw import *
from base_words import *

router = Router()

@router.message(F.text == "/start")
async def start_handler(message: Message):
    await message.answer(START_TEXT, reply_markup=main)

@router.message(F.text == "/about")
async def about_handler(message: Message):
    await message.answer(ABOUT_TEXT)

@router.message(F.text == "/help")
async def help_handler(message: Message):
    await message.answer(HELP_TEXT)