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
                text="Вторник:\n----\n1️⃣ -\n2️⃣ Русский\n3️⃣ Литература\n4️⃣ Химия\n5️⃣ ФЛ/Физика\n6️⃣ ФЛ/Физика\n7️⃣ ФЛ/Физика\n8️⃣ФЛ/Физика")
        case 'wednesday':
            await callback.message.edit_text(
                text="Среда:\n----\n1️⃣ Мат анализ\n2️⃣ Мат анализ\n3️⃣ Химия\n4️⃣ Биология\n5️⃣ ТВиС\n6️⃣ Англ яз\n7️⃣ Литература")
        case 'thursday':
            await callback.message.edit_text(
                text="Четверг:\n----\n1️⃣ История\n2️⃣ История\n3️⃣ ОБЖ\n4️⃣ Общ\n5️⃣ Общ\n6️⃣ Физ-ра\n7️⃣ Физ-ра")
        case 'friday':
            await callback.message.edit_text(
                text="Пятница:\n----\n1️⃣ Физика\n2️⃣ Физика\n3️⃣ Мат анализ\n4️⃣ Мат анализ\n5️⃣ Информ\n6️⃣ Информ")
        case 'saturday':
            await callback.message.edit_text(
                text="Суббота:\n----\n1️⃣ -\n2️⃣ География\n3️⃣ Англ яз\n4️⃣ Англ яз\n5️⃣ Геометрия\n6️⃣ Геометрия\n7️⃣ Геометрия")


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
