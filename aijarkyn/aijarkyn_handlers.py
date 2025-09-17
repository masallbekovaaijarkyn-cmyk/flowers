from aiogram import Router, F
from aiogram.types import Message, FSInputFile

from aijarkyn_keyboards import menu
from aijarkyn_words import START_TEXT, TEAM_TEXT

router = Router()

@router.message(F.text == "/start")
async def start(message: Message):
    await message.answer(START_TEXT, reply_markup=menu)

@router.message(F.text == "/team")
async def team(message: Message):
    await message.answer(TEAM_TEXT)


    photo = FSInputFile("pp.jpg")
    await message.answer_photo(
        photo=photo,
        caption="Айжаркын✨"
    )

    photo2 = FSInputFile("yy.jpeg")
    await message.answer_photo(
        photo=photo2,
        caption="AIDAR"
    )


    photo3 = FSInputFile("jpeg(1)")
    await message.answer_photo(
        photo=photo3,
        caption="AISARA"
    )


    photo4 = FSInputFile("jpeg(4)")
    await message.answer_photo(
        photo=photo4,
        caption="YRYS"
    )


    photo5 = FSInputFile("jpeg(2)")
    await message.answer_photo(
        photo=photo5,
        caption="AIBIIKE"
    )


    photo6 = FSInputFile("jpeg(3)")
    await message.answer_photo(
        photo=photo6,
        caption="NAZIMA"
    )
@router.message(F.text == "menuu")
async def menuu(message: Message):
    await message.answer("Вы вернулись в меню 👇", reply_markup=menu)