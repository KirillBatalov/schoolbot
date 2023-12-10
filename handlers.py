from aiogram import Router, F
from aiogram.filters import Command, Text, callback_data
from aiogram.types import *
from aiogram.utils.keyboard import InlineKeyboardBuilder

from db_controller import DatabaseController

router = Router()


@router.message(Command(commands=["start"]))
async def command_start(message: Message):
    user = DatabaseController.get_user(message.from_user.id)
    if user is None:
        grade_keyboards = InlineKeyboardBuilder()
        for key, value in DatabaseController.get_grades().items():
            grade_keyboards.row(InlineKeyboardButton(text=key, callback_data=f'grade_{value}'))
        await message.answer(text="Выберите класс", reply_markup=grade_keyboards.as_markup())
    else:
        keyboard = ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text='Расписание уроков'), KeyboardButton(text='Расписание звонков')]])
        await message.answer(text="Добро пожаловать!", reply_markup=keyboard)

@router.callback_query(F.data.startswith('grade'))
async def add_user(callback: CallbackQuery):
    grade_id = callback.data.split('_')[1]
    DatabaseController.add_user(callback.from_user.id, int(grade_id))


@router.message(F.text == 'Расписание уроков')
async def lesson_schedule(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text='Понедельник', callback_data='day_1')],
                         [InlineKeyboardButton(text='Вторник', callback_data='day_2')],
                         [InlineKeyboardButton(text='Среда', callback_data='day_3')],
                         [InlineKeyboardButton(text='Четверг', callback_data='day_4')],
                         [InlineKeyboardButton(text='Пятница', callback_data='day_5')],
                         [InlineKeyboardButton(text='Суббота', callback_data='day_6')]])
    await message.answer(text='Выберите день', reply_markup=keyboard)


@router.callback_query(F.data.startswith('day'))
async def select_day(callback: CallbackQuery):
    day = callback.data.split('_')[1]
    e = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣']
    a = ""
    lessons = DatabaseController.get_lessons(callback.from_user.id, day)
    for lesson_number, lesson_name in lessons.items():
        a += f'{e[lesson_number - 1]} {lesson_name}\n'
    await callback.message.edit_text(text=a)

@router.message(F.text == 'Расписание звонков')
async def ringings_schedule(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text='Средний проспект', callback_data='street_sred')],
                         [InlineKeyboardButton(text='ул. Шевченко д.23', callback_data='street_schev')]])
    await message.answer(text='Выберите здание', reply_markup=keyboard)


@router.callback_query(F.data.startswith('street'))
async def select_street(callback: CallbackQuery):
    street = callback.data.split('_')[1]
    match street:
        case 'sred':
            await callback.message.edit_text(
                text="1. 08:30-09:15\n2. 09:25-10:10\n3. 10:25-11:10\n4. 11:30-12:15\n5. 12:35-13:20\n6. 13:35-14:20\n7. 14:30-15:15\n8. 15:25-16:10")
        case 'schev':
            await callback.message.edit_text(
                text="1. 08:50-9:35\n2. 09:45-10:30\n3. 10:45-11:30\n4. 11:50-12:35\n5. 12:55-13:40\n6. 13:55-14:40\n7.  14:50-15:35")
