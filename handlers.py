from aiogram import Router, F
from aiogram.filters import Command, Text
from aiogram.types import *


router = Router()

@router.message(Command(commands=["start"]))
async def command_start(message: Message):
    await message.answer(text="Добро пожаловать!")