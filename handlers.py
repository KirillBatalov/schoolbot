from aiogram import Router, F
from aiogram.filters import Command, Text, callback_data
from aiogram.types import *

router = Router()


@router.message(Command(commands=["start"]))
async def command_start(message: Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text='Расписание уроков'), KeyboardButton(text='Расписание звонков')]])
    await message.answer(text="Добро пожаловать!", reply_markup=keyboard)


@router.message(F.text == 'Расписание уроков')
async def lesson_schedule(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text='Понедельник', callback_data='day_monday')],
                         [InlineKeyboardButton(text='Вторник', callback_data='day_tuesday')],
                         [InlineKeyboardButton(text='Среда', callback_data='day_wednesday')],
                         [InlineKeyboardButton(text='Четверг', callback_data='day_thursday')],
                         [InlineKeyboardButton(text='Пятница', callback_data='day_friday')],
                         [InlineKeyboardButton(text='Суббота', callback_data='day_saturday')]])
    await message.answer(text='Выберите день', reply_markup=keyboard)


@router.callback_query(F.data.startswith('day'))
async def select_day(callback: CallbackQuery):
    day = callback.data.split('_')[1]
    match day:
        case 'monday':
            await callback.message.edit_text(
                text="Понедельник:\n----\n1️⃣ РоВ\n2️⃣ Физика\n3️⃣ Алгебра\n4️⃣ Алгебра\n5️⃣ Алгебра\n6️⃣ Русский\n7️⃣ Литература")
        case 'tuesday':
            await callback.message.edit_text(
                text="Вторник:\n----\n1.-\n2.Русский\n3.Литература\n4.Химия\n5.ФЛ/Физика\n6.ФЛ/Физика\n7.ФЛ/Физика\n8.ФЛ/Физика")
        case 'wednesday':
            await callback.message.edit_text(
                text="Среда:\n----\n1.Мат анализ\n2.Мат анализ\n3.Химия\n4.Биология\n5.ТВиС\n6.Англ яз\n7.Литература")
        case 'thursday':
            await callback.message.edit_text(
                text="Четверг:\n----\n1.История\n2.История\n3.ОБЖ\n4.Общ\n5.Общ\n6.Физ-ра\n7.Физ-ра")
        case 'friday':
            await callback.message.edit_text(
                text="Пятница:\n----\n1.Физика\n2.Физика\n3.Мат анализ\n4.Мат анализ\n5.Информ\n6.Информ")
        case 'saturday':
            await callback.message.edit_text(
                text="Суббота:\n----\n1.-\n2.География\n3.Англ яз\n4.Англ яз\n5.Геометрия\n6.Геометрия\n7.Геометрия")
