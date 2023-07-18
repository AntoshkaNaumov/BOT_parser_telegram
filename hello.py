from datetime import datetime, timedelta
from pyrogram import Client, filters, emoji, types
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton)


api_id = 21406080
api_hash = '38e2538270867e3c7ebcc3085f744583'
bot_token = "6370592266:AAHEPh21W--k1Xzt7o9Wxrm-2bWwO-0jzoA"
app = Client("my_bot", api_id=api_id, api_hash=api_hash,
             bot_token=bot_token
             )


# Демонстрация эхо бота
#@app.on_message(filters.text & filters.private)
#async def echo(client, message):
#    await message.reply(message.text)


# обрабатывать запросы обратного вызова, т. е. запросы, поступающие от встроенных нажатий кнопок
#@app.on_callback_query()
#async def answer(client, callback_query):
#    await callback_query.answer(
#        f"Button contains: '{callback_query.data}'",
#        show_alert=True)


# Функция для отправки сообщения с inline-кнопкой
#@app.on_message(filters.command(["start"]))
#async def start(client, message):
    # Создаем inline-кнопку
#    button = types.InlineKeyboardButton("Нажми меня", callback_data="button_clicked")
#    inline_keyboard = types.InlineKeyboardMarkup([[button]])

    # Отправляем сообщение с кнопкой пользователю
#    await message.reply_text("Привет! Нажми на кнопку.", reply_markup=inline_keyboard)


@app.on_message(filters.command('start'))
def start(client, message):
    # Get the current date
    today = datetime.now().date()

    # Calculate the start and end timestamps for the day
    start_timestamp = int((datetime(today.year, today.month, today.day) - timedelta(days=1)).timestamp())
    end_timestamp = int(datetime(today.year, today.month, today.day).timestamp())

    # Retrieve all messages from all user chats within the specified day
    dialogs = client.iter_dialogs()
    for dialog in dialogs:
        chat = dialog.chat
        if chat.type == "private":
            messages = client.get_chat_history(chat.id, limit=10000, offset_date=start_timestamp, until_date=end_timestamp)
            for message in messages:
                print(message.text)


@app.on_message(filters.command('help'))
def help_command(client, message):
    # Provide help with command descriptions
    help_text = "Available commands:\n" \
                "/start - Retrieve all messages from all user chats per day\n" \
                "/help - Display available commands and descriptions"
    client.send_message(chat_id=message.chat.id, text=help_text)


app.run()
