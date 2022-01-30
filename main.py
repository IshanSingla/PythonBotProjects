from datetime import datetime
import json, firebase_admin, sys,telethon,asyncio,requests
from tokenize import Token
from telethon import *
import logging
import os
from asyncio import sleep

from telethon import functions, types
from telethon import TelegramClient, events, Button
from telethon.sessions import StringSession
from telethon.errors.rpcerrorlist import ChatAdminRequiredError
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins, ChatAdminRights
from telethon.tl.functions.channels import EditBannedRequest
from decouple import config

import logging
import os
from asyncio import sleep

from decouple import config

from telethon import TelegramClient, events, Button
from telethon.sessions import StringSession
from telethon.errors.rpcerrorlist import ChatAdminRequiredError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights



from telethon.errors.rpcerrorlist import ChatAdminRequiredError
from firebase_admin import credentials,db
cred = credentials.Certificate('1.json')
default_app = firebase_admin.initialize_app( cred,{'databaseURL':"https://induced-scraping-bot-30ee0-default-rtdb.asia-southeast1.firebasedatabase.app/"})


APP_ID = 12468937
API_HASH = "84355e09d8775921504c93016e1e9438"
BOT_TOKEN = "5170782972:AAFba1KKvu7DzcX_4utjQqzRVidmurFMCbE"
OWNERS=[1854668908, 1303790979, 1322941082, 5217968098]
SESSION = config("SESSION")
#client = telethon.TelegramClient("cli", api_id=APP_ID , api_hash=API_HASH).start(bot_token=BOT_TOKEN)

try:
    client = TelegramClient(
        StringSession(SESSION), api_id=API_ID, api_hash=API_HASH).start()

except Exception as e:
    log.warning(e)
    exit(1)
    
    
try:
    bot = TelegramClient(None, api_id=API_ID, api_hash=API_HASH).start(bot_token=BOT_TOKEN)

except Exception as e:
    logging.warning(e)
    exit(1)   
    



@bot.on(events.NewMessage(incoming=True, pattern=r"\.adding"))
async def _(e):
    if e.sender_id in OWNERS:
        TOK=(db.reference(f"/Members/Tok/")).get()
        LINK=(db.reference(f"/Members/Link/")).get()
        await e.reply(f"Adding Start")
        while True:
            for x in TOK:
                for i in LINK:
                    get_ip= requests.get(f"https://telesubs.com/api/v2?key={x}&action=add&service=56&link={i}&quantity=50")
                    red = json.loads(get_ip.text)
                    if 'error' in red:
                        if red['error']=="You have active order with this link. Please wait until order being completed.":
                            pass
                        else:
                            await e.reply(f"Error:  `{red['error']}`\n\nToken: {x}\n\nMade with ❤️ By @InducedBots")
                            return
                    else:
                        await e.reply(f"Order ID:  `{red['order']}`\nOrder Link: {i}\nOrder Token: `{x}`\n\nMade with ❤️ By @InducedBots")
            await asyncio.sleep(5)
    else:
        await e.reply("You can not use me\nContact: @IshanSingle_xD\n\nMade with ❤️ By @InducedBots")

@bot.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
async def ping(e):
    if e.sender_id in OWNERS:
        start = datetime.now()
        text = "Pong! \nBy Induced"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"(●'◡'●) 𝗣𝗼𝗻𝗴!\n`{ms}` 𝗺𝘀 \n\nMade with ❤️ By @InducedBots")
    else:
        await e.reply("You can not use me\nContact: @IshanSingle_xD\n\nMade with ❤️ By @InducedBots")

@bot.on(events.NewMessage(incoming=True, pattern=r"\.restart"))    
async def restart(e):
    await e.reply("**Bot Is Restarting...\n\nMade with ❤️ By @InducedBots**")
    os.execl(sys.executable, sys.executable, "-m", "main")

    
#approve admin from here     
    
async def get_waiting(chat_id):
    try:
        users = await client(
            functions.messages.GetChatInviteImportersRequest(
                requested=True,
                peer=chat_id,
                limit=0,
                offset_date=0,
                offset_user=types.InputPeerEmpty(),
            )
        )
    except ChatAdminRequiredError:
        me = await client.get_me()
        return (
            "Chat Admin required [{}](tg://user?id={}).".format(
                me.first_name, me.id
            ),
            [],
        )
    if users.count == 0:
        return "Nothing here to approve !", []
    userids = [i.user_id for i in users.importers]
    return "**Total no of user who requesting to join**: {}\n\n".format(users.count), userids


@bot.on(events.NewMessage(incoming=True, pattern="^/waiting", from_users=OWNERS))
async def reply_waits(event):
    mid = chat = None
    if event.is_private:
        try:
            mid = event.text.split(" ")[1]
        except IndexError:
            await event.reply(
                "Please provide a chat ID or username, or use this command in that chat/channel."
            )
            return
    else:
        mid = event.chat_id
    try:
        mid = int(mid)
        chat = (await client.get_entity(mid)).id
    except ValueError:
        chat = (await client.get_entity(mid)).id
    msg, users = await get_waiting(chat)
    await event.reply(msg)


@bot.on(events.NewMessage(incoming=True,from_users=OWNERS,pattern="^/approveall",))
async def approvealll(event):
    mid = chat = None
    xx = await event.reply("Hold on.")
    if event.is_private:
        try:
            mid = event.text.split(" ")[1]
        except IndexError:
            await xx.edit(
                "Please provide a chat ID or username, or use this command in that chat/channel."
            )
            return
    else:
        mid = event.chat_id
    try:
        mid = int(mid)
        chat = (await client.get_entity(mid)).id
    except ValueError:
        chat = (await client.get_entity(mid)).id
    msg, users = await get_waiting(chat)
    if msg.startswith("Please") or msg.startswith("No"):
        await xx.edit(msg)
        return
    else:
        dn = fail = 0
        err = None
        while len(users) > 0:
            for i in users:
                try:
                    await client(
                        functions.messages.HideChatJoinRequestRequest(
                            chat, user_id=int(i), approved=True
                        )
                    )
                    dn += 1
                except Exception as e:
                    fail += 1
                    err = e
            msg, users = await get_waiting(chat)
            if msg.startswith("Please") or msg.startswith("No"):
                await xx.edit(msg)
                break
        msg = "__Approved {} user(s).__".format(dn)
        if fail != 0:
            msg += "\n__Failed to approve {} user(s).__".format(fail)
            msg += "\n\n**Logs Forward this to @Vexana_Support**: {}".format(err)
    await xx.edit(msg)


@bot.on(events.NewMessage(incoming=True,from_users=OWNERS,pattern="^/disapproveall",))
async def approvealll(event):
    mid = chat = None
    if event.is_private:
        try:
            mid = event.text.split(" ")[1]
        except IndexError:
            await event.reply(
                "Please provide a chat ID or username, or use this command in that chat/channel."
            )
            return
    else:
        mid = event.chat_id
    try:
        mid = int(mid)
        chat = (await client.get_entity(mid)).id
    except ValueError:
        chat = (await client.get_entity(mid)).id
    msg, users = await get_waiting(chat)
    if msg.startswith("Please") or msg.startswith("No"):
        await event.reply(msg)
        return
    else:
        dn = fail = 0
        err = None
        for i in users:
            try:
                await client(
                    functions.messages.HideChatJoinRequestRequest(
                        chat, user_id=int(i), approved=False
                    )
                )
                dn += 1
            except Exception as e:
                fail += 1
                err = e
        msg = "__Disapproved {} user(s).__".format(dn)
        if fail != 0:
            msg += "\n__Failed to disapprove {} user(s).__".format(fail)
            msg += "\n\n**Logs Forward this to @Vexana_Support**: {}".format(err)
    await event.reply(msg)


  

print("""
┏━━┓      ┏┓              ┏┓    ┏━━┓        ┏━━━┓    ┏┓           
┗┫┣┛      ┃┃              ┃┃    ┗┫┣┛        ┃┏━┓┃    ┃┃           
 ┃┃ ┏━┓ ┏━┛┃┏┓┏┓┏━━┓┏━━┓┏━┛┃     ┃┃ ┏━━┓    ┃┃ ┃┃┏━┓ ┃┃ ┏┓┏━┓ ┏━━┓
 ┃┃ ┃┏┓┓┃┏┓┃┃┃┃┃┃┏━┛┃┏┓┃┃┏┓┃     ┃┃ ┃━━┫    ┃┃ ┃┃┃┏┓┓┃┃ ┣┫┃┏┓┓┃┏┓┃
┏┫┣┓┃┃┃┃┃┗┛┃┃┗┛┃┃┗━┓┃┃━┫┃┗┛┃    ┏┫┣┓┣━━┃    ┃┗━┛┃┃┃┃┃┃┗┓┃┃┃┃┃┃┃┃━┫
┗━━┛┗┛┗┛┗━━┛┗━━┛┗━━┛┗━━┛┗━━┛    ┗━━┛┗━━┛    ┗━━━┛┗┛┗┛┗━┛┗┛┗┛┗┛┗━━┛
Induced Adding Started Sucessfully........
""")
if len(sys.argv) not in (1, 3, 4):
    try:
        client.disconnect()
    except Exception as e:
            pass
else:
    try:
        client.run_until_disconnected()
        except Exception as e:
        pass
