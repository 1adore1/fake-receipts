import logging
import asyncio
from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import re


logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())
router = Router()
dp.include_router(router)

class Form(StatesGroup):
    name = State()
    phone = State()
    amount = State()

def create_image(user_id, name, phone, amount):
    amount = str(amount)
    numbers = phone.split()
    phone = f'+7 {numbers[0]} {numbers[1]}-{numbers[2]}-{numbers[3]}'
    img = Image.open('source_image.png')
    draw = ImageDraw.Draw(img)
    
    font_amount = ImageFont.truetype("fonts/TinkoffSans-Bold.ttf", 53)
    font_phone = ImageFont.truetype("fonts/TinkoffSans-Regular.ttf", 29)
    font_name = ImageFont.truetype("fonts/TinkoffSans-Regular.ttf", 28)
    font_time = ImageFont.truetype("fonts/SF-Pro-Display-Bold.otf", 28)

    img_width, img_height = img.size

    def centered_coords(text, font, y_coord):
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        x_coord = (img_width - text_width) // 2
        return x_coord, y_coord

    name_coords = centered_coords(name, font_name, 483)
    phone_coords = centered_coords(phone, font_phone, 662)
    amount_coords = centered_coords(f"–{amount} ₽", font_amount, 380)
    time_coords = (61, 22)

    current_time = datetime.now()
    formatted_time = current_time.strftime("%H:%M")

    draw.text(name_coords, name, font=font_name, fill=(60, 42, 40))
    draw.text(phone_coords, phone, font=font_phone, fill=(71, 71, 71))
    draw.text(amount_coords, f"–{amount} ₽", font=font_amount, fill=(252, 252, 252))
    draw.text(time_coords, formatted_time, font=font_time, fill=(255, 255, 255))

    output_path = f'imgs/{user_id}.png'
    img.save(output_path)
    return output_path

def get_receipt_keyboard(user_id):
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text='New receipt', callback_data='new_receipt'))
    return builder.as_markup()

@router.message(Command('start'))
async def start_command(message: types.Message):
    user_id = message.chat.id
    await message.answer('A bot for creating fake transfer screenshots.', reply_markup=get_receipt_keyboard(user_id))

@router.message(Command('new'))
async def new_command(message: types.Message, state: FSMContext):
    user_id = message.chat.id
    await bot.send_message(user_id, 'Enter first and last name (Ivan I.): ')
    await state.set_state(Form.name)

@router.callback_query(F.data == 'new_receipt')
async def start_receipt(callback_query: types.CallbackQuery, state: FSMContext):
    user_id = callback_query.message.chat.id
    await bot.send_message(user_id, 'Enter first and last name (Ivan I.): ')
    await state.set_state(Form.name)

@router.message(Form.name)
async def process_name(message: types.Message, state: FSMContext):
    name = message.text
    if not re.match(r'^[А-ЯЁа-яёA-Za-z. ]+$', name):
        await message.answer('The name must contain only letters, spaces, and a period. Try again. ')
        return
    await state.update_data(name=name)
    await message.answer('Enter the phone number (123 456 78 90): ')
    await state.set_state(Form.phone)

@router.message(Form.phone)
async def process_phone(message: types.Message, state: FSMContext):
    phone = message.text
    if not re.match(r'^\d{3} \d{3} \d{2} \d{2}$', phone):
        await message.answer('The phone should be in the format 123 456 78 90. Try again. ')
        return
    await state.update_data(phone=phone)
    await message.answer('Enter the amount: ')
    await state.set_state(Form.amount)

@router.message(Form.amount)
async def process_amount(message: types.Message, state: FSMContext):
    amount = message.text
    if not amount.isdigit() or int(amount) <= 0:
        await message.answer('The sum must be a positive number. Try again.')
        return
    user_id = message.chat.id
    user_data = await state.get_data()
    name = user_data['name']
    phone = user_data['phone']

    image_path = create_image(user_id, name, phone, amount)
    photo = types.FSInputFile(image_path)
    await bot.send_photo(user_id, photo, reply_markup=get_receipt_keyboard(user_id))

    await state.clear()

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
