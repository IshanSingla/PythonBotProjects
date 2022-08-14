# Anonymize - Forward tag remover bot
# Copyright (C) 2021 @IshanSingla | @Itz_Alain
#
# This file is a part of < https://github.com/IshanSingla/TgForwardTagRemover/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/IshanSingla/TgForwardTagRemover/blob/main/LICENSE/>.

import re, os, random, asyncio, html
os.system("pip install pyrogram")
import pyrogram
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

APP_ID = os.environ.get("APP_ID")
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

app = pyrogram.Client("app", api_id=APP_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

but = InlineKeyboardMarkup([[InlineKeyboardButton("Help 🤔", callback_data="Help"), InlineKeyboardButton("Close 🔐", callback_data="close")],[InlineKeyboardButton("Updates ⬆", url="https://t.me/InducedBotUpdates"), InlineKeyboardButton("Developer 💕", url="t.me/IshanSingla")]])
butt = InlineKeyboardMarkup([[InlineKeyboardButton("Home 🏠", callback_data="home"), InlineKeyboardButton("Updates ⬆", url="https://t.me/InducedBotUpdates")], [InlineKeyboardButton("Repo 👉", url="GitHub.com/IshanSingla/TgForwardTagRemover"), InlineKeyboardButton("Close 🔐", callback_data="close")]])


@app.on_message(filters.command(["start"]))
async def start(lel, message):
    await message.reply_text(f"**Hi** `{message.from_user.first_name}` **!\n\nI'm any forward tag remover // anonymize bot! I can send the file which you sended to me, without forward tag..!\nMade with ❤️ By Induced**", reply_markup=but)

@app.on_message(filters.command(["help"]))
async def help(ha, message):
    await app.send_message(message.chat.id, """**There is nothing no more..!\nJust forward me any file // message and I will return it back without forwaded tag.\n\nMade with ❤️ By Induced**""", reply_markup=butt) 

@app.on_callback_query()
async def button(app, update):
    k = update.data
    if "Help" in k:
       await update.message.delete()
       await help(app, update.message)
    elif "close" in k:
       await update.message.delete()
    elif "home" in k:
       await update.message.delete()
       await start(app, update.message)

@app.on_message(filters.private)
async def copy(sed, message):
    try:
       await message.copy(message.chat.id)
    except RCPError as lel:
       await message.reply(lel)
       return


print("Your Bot Was Successfully Started!") 
print("Join @InducedBotSupport for any help...!")
app.run()
