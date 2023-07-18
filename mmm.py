import asyncio
from datetime import datetime, timedelta
from pyrogram import Client, filters, errors
from pyrogram.handlers import MessageHandler
from pyrogram.errors import RPCError
from config import api_id, api_hash


# Target channel/supergroup
TARGET = -1001231772809
# Create a Pyrogram client

app = Client('my_session')


# Получить все свои чаты
async def main():
    async with app:
        async for dialog in app.get_dialogs():
            print(dialog.chat.title, dialog.chat.first_name, dialog.chat.id)


# Получить всех участников чата по id чата
async def main2():
    async with app:
        async for member in app.get_chat_members(TARGET):
            print(member)


# В этом примере показано, как запросить встроенного бота (от имени пользователя)
async def main3():
    async with app:
        # Get bot results for "hello" from the inline bot @vid
        bot_results = await app.get_inline_bot_results("vid", "тайланд")

        # Send the first result to your own chat (Saved Messages)
        await app.send_inline_bot_result(
            "me", bot_results.query_id,
            bot_results.results[0].id)


# В этом примере показано, как обрабатывать необработанные обновления
#@app.on_raw_update()
#async def raw(client, update, users, chats):
#    print(update)


async def main4():
    async with app:

        await app.set_profile_photo(photo="2MsxDRdPFQQ.jpg")

app.run()
