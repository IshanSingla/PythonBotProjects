from datetime import datetime
import json, firebase_admin, sys,telethon,asyncio,requests,os
from firebase_admin import credentials,db
cred = credentials.Certificate('1.json')
default_app = firebase_admin.initialize_app( cred,{'databaseURL':"https://induced-scraping-bot-30ee0-default-rtdb.asia-southeast1.firebasedatabase.app/"})
APP_ID = 12468937
API_HASH = "84355e09d8775921504c93016e1e9438"
BOT_TOKEN = "5170782972:AAFba1KKvu7DzcX_4utjQqzRVidmurFMCbE"
OWNERS=[1854668908, 1303790979, 1322941082, 5217968098]
client = telethon.TelegramClient(None, api_id=APP_ID , api_hash=API_HASH).start(bot_token=BOT_TOKEN)
client.send_message("@InducedSpam","Hlo Everyone I am back Online\n\nCommand:\n\n`.start` to Start Adding`.check <order_id> <api_token>`\n\n`.ping` to Check Ping\n`.restart` to Restart Bot\n\nMade with ❤️ By @InducedBots")

@client.on(telethon.events.NewMessage(incoming=True, pattern=r"\.start"))
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

@client.on(telethon.events.NewMessage(incoming=True, pattern=r"\.ping"))
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

@client.on(telethon.events.NewMessage(incoming=True, pattern=r"\.restart"))    
async def restart(e):
    await e.reply("**Bot Is Restarting...\n\nMade with ❤️ By @InducedBots**")
    os.execl(sys.executable, sys.executable, "-m", "main")

@client.on(telethon.events.NewMessage(incoming=True, pattern=r"\.check"))
async def _(e):
    if e.sender_id in OWNERS:
        isha = e.text.split(" ")
        if len(isha) ==2:
            get_ip= requests.get(f"https://telesubs.com/api/v2?key={isha[1]}apikey&action=status&order={isha[0]}")
            red = json.loads(get_ip.text)
            try:
                await e.reply(f"*✳Info Extracted*\n---------\n📦Order Status : {red['status']}\n🧾Remains : {red['remains']}\n\nMade with ❤️ By @InducedBots")
            except:
                await e.reply("You may put wrong Id's or Wromg Method\nCommand:\n\n`.check <order_id> <api_token>`\n\nMade with ❤️ By @InducedBots")
        else:
            await e.reply("𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = Check\nCommand:\n\n`.check <order_id> <api_token>`\n\nMade with ❤️ By @InducedBots")
    else:
        await e.reply("You can not use me\nContact: @IshanSingle_xD\n\nMade with ❤️ By @InducedBots")
print("""
╔════╗
╚═╗╔═╝
╔═╣╠═╗
║╔╣╠╗║
║╚╣╠╝║
╚═╣╠═╝
╔═╝╚═╗
╚════╝""")
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
