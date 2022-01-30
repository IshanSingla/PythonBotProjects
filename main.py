import json, firebase_admin, sys,telethon,asyncio,requests
from tokenize import Token
from telethon import *

from firebase_admin import credentials,db
cred = credentials.Certificate('1.json')
default_app = firebase_admin.initialize_app( cred,{'databaseURL':"https://induced-scraping-bot-30ee0-default-rtdb.asia-southeast1.firebasedatabase.app/"})


APP_ID = 12468937
API_HASH = "84355e09d8775921504c93016e1e9438"
BOT_TOKEN = "5170782972:AAFba1KKvu7DzcX_4utjQqzRVidmurFMCbE"
OWNERS=[1854668908, 1303790979, 1322941082]
client = telethon.TelegramClient("cli", api_id=APP_ID , api_hash=API_HASH).start(bot_token=BOT_TOKEN)



@client.on(events.NewMessage(incoming=True, pattern=r"\.adding"))
async def _(e):
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
                        await e.reply(f"Order ID:  `{red['order']}`\nOrder Link: `{i}`\nOrder Token: `{x}`\n\nMade with ❤️ By @InducedBots")
            await asyncio.sleep(5)

"""
@client.on(events.NewMessage(incoming=True,pattern="?/approveall",))
async def approvealll(event):
    mid = chat = None
    xx = await event.reply("Hold on.")
    if event.is_private:
        try:
            mid = event.text.split(" ")[1]
        except IndexError:
            await xx.edit("Please provide a chat ID or username, or use this command in that chat/channel.")
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
                    await client(functions.messages.HideChatJoinRequestRequest(chat, user_id=int(i), approved=True ))
                    dn += 1
                except Exception as e:
                    fail += 1
                    err = e
            msg, users = await get_waiting(chat)
            if msg.startswith("Please") or msg.startswith("No"):
                await xx.edit(msg)
                break
        msg = "Approved {} user(s).".format(dn)
        if fail != 0:
            msg += "\n__Failed to approve {} user(s).__".format(fail)
    await xx.edit(msg)
"""


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
