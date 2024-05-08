from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyboards as kb

router = Router()


class Register(StatesGroup):
    name = State()
    age = State()
    number = State()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer("Здравствуйте!", reply_markup=kb.main)


@router.message(F.text == "Каталог")
async def catalog(message: Message):
    await message.answer("Выберите категорию товара", reply_markup=kb.catalog)


@router.callback_query(F.data == "t_shirt")
async def t_shirt(callback: CallbackQuery):
    await callback.answer("Вы выбрали категорию", show_alert=True)
    await callback.message.answer("Вы выбрали категорию футболок")


@router.callback_query(F.data == "sneakers")
async def t_shirt(callback: CallbackQuery):
    await callback.answer("Вы выбрали категорию", show_alert=True)
    await callback.message.answer("Вы выбрали категорию кроссовок")


@router.callback_query(F.data == "cap")
async def t_shirt(callback: CallbackQuery):
    await callback.answer("Вы выбрали категорию", show_alert=True)
    await callback.message.answer("Вы выбрали категорию кепок")


@router.message(Command("register"))
async def register(message: Message, state: FSMContext):
    await state.set_state(Register.name)
    await message.answer("Введите ваше имя")


@router.message(Register.name)
async def register_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Register.age)
    await message.answer("Введите ваш возраст")


@router.message(Register.age)
async def register_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Register.number)
    await message.answer("Отправьте ваш номер телефона", reply_markup=kb.get_number)


@router.message(Register.number, F.contact)
async def register_number(message: Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(
        f'Ваше имя: {data["name"]}\nВаш возраст: {data["age"]}\nВаш номер телефона: {data["number"]}'
    )
    await state.clear()
