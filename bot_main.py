import logging
import os
import pandas as pd
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import executor
from flask import Flask


app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)
token = "6370592266:AAHEPh21W--k1Xzt7o9Wxrm-2bWwO-0jzoA"



bot = Bot(token=token)
dp = Dispatcher(bot, storage=MemoryStorage())

# Handler for the "Парсинг данных" command
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=2)
    buttons = [
        types.KeyboardButton(text="Запустить парсинг данных"),
        types.KeyboardButton(text="Получить файл с данными"),
        types.KeyboardButton(text="Help"),
    ]
    keyboard_markup.add(*buttons)
    await message.answer("Привет! Что ты хочешь сделать?", reply_markup=keyboard_markup)

@dp.message_handler(lambda message: message.text == "Запустить парсинг данных")
async def parsing_data(message: types.Message):
    # Отправляем сообщение с информацией о начале сбора данных
    await message.reply("Начинаю сбор данных с ваших чатов. Сбор данных с учетом фильтров займет примерно 16 минут")

    # Тут выполняется команда для запуска скрипта по сбору данных
    os.system('python test.py')

@dp.message_handler(lambda message: message.text == "Получить файл с данными")
async def get_data(message: types.Message):
    try:
        df = pd.read_excel('messages.xlsx')  # Открытие файла messages.xlsx
        with open('messages.xlsx', 'rb') as f:
            await message.answer_document(document=f, caption='messages.xlsx')  # Отправка файла Excel в качестве документа
    except FileNotFoundError:
        await message.answer("Файл отсутствует. Повторите запрос")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

# Handler for the "Help" button
@dp.message_handler(lambda message: message.text == "Help")
async def help(message: types.Message):
    await message.answer("Помощь по использованию бота:\n"
                        "1. Команда /start - запуск бота\n"
                        "2. Кнопка 'Запустить парсинг данных' - запуск парсинга сообщений чата\n"
                        "3. Кнопка 'Получить файл с данными' - получение xlsx файла от бота\n"
                        "4. Кнопка 'Help' - отображение справочной информации")

@dp.message_handler()
async def handle_unknown_command(message: types.Message):
    await message.answer("Бот не знает данной команды. Обратитесь к команде help")


@app.route('/')
async def run_bot():
    await bot.send_message(chat_id='YOUR_CHAT_ID', text='Bot is running')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    app.run()
