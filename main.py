import json, sys,telethon,asyncio,requests,os,time, psutil
from telethon import events, Button
APP_ID = 12468937
API_HASH = "84355e09d8775921504c93016e1e9438"
BOT_TOKEN = "5170782972:AAFba1KKvu7DzcX_4utjQqzRVidmurFMCbE"
OWNERS=[1682948336, 1303790979]
client = telethon.TelegramClient(None, api_id=APP_ID , api_hash=API_HASH).start(bot_token=BOT_TOKEN)
start_time=time.time()
Data={}


async def start_Ustad():
    await client.send_message(1303790979,"Now I am Restarted\n\nMade with ❤️ By @InducedBots")

loop = asyncio.get_event_loop()
loop.run_until_complete(start_Ustad())

@client.on(events.NewMessage(incoming=True, pattern='/start'))
async def _(e):
    but=[
            [
                Button.inline("Instagram", b"Instagram"),
                Button.inline("Telegram", b"Telegram") 
            ],
            [
                Button.url("Support ☎️", url=f"https://t.me/InducedBotsSupport"),
                Button.inline("AdminPannel 🛰", b"Admin")
            ]
        ]
    await client.send_message(e.chat.id,f"**Welcome Sir!\n\nI'm Induced Members Bot \nMade for Adding Members\\Like\\Comments\\Vots\n\nMade with ❤️ By @InducedBots**", buttons=but)



# <---------------- Instagram ---------------->
@client.on(events.CallbackQuery)
async def handler(e):
    if e.data == b'Instagram':
        but=[
                [
                    Button.inline("SpeedFollow", b"SpeedFollow"),
                    Button.inline("None", b"None") 
                ],
                [
                    Button.inline("Back", b"Home")
                ]
            ]
        await client.edit_message(e.chat.id, e.query.msg_id,f"**Welcome Sir!\n\nI'm Induced Members Bot \nMade for Adding Members\\Like\\Comments\\Vots\n\nMade with ❤️ By @InducedBots**", buttons=but)

    elif e.data == b'SpeedFollow':
        if e.query.user_id in OWNERS:
            await e.answer('\nWelcome To SpeedFollow', alert=True)
            but=[
                    [
                        Button.inline("Start", b"FollowStrt"),
                        Button.inline("Stats", b"FollowCheck")
                    ],
                    [
                        Button.inline("Back", b'Instagram')
                    ]
                ]
            await client.edit_message(e.chat.id, e.query.msg_id,f"**Welcome Sir!\n\nI'm Induced Members Bot \nMade for Adding Members\\Like\\Comments\\Vots\n\nMade with ❤️ By @InducedBots**", buttons=but)
        else:
            await e.answer('\n\n\n\nYou have access of me Contact @IshanSingle_xD', alert=True)

    elif e.data == b'FollowStrt':
        if e.query.user_id in OWNERS:
            await e.answer('\nAdding Start Check Stats for info', alert=True)
            async with client.conversation(e.chat_id) as x:
                await x.send_message(f"Please Send You User Id")
                id = await x.get_response()
                await x.send_message(f"Please Send You Auth Token")
                auth = await x.get_response()
            your_header = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
            get_ip=requests.get(method='GET',url=f"https://technicaldebayan.net.in//Scripts/dir----oct-----110--!@/speedfollow/?timer=3&cd=follow&usid={id.text}&auth={auth.text}&submit=submit",headers=your_header,timeout=999999999)
            #get_ip = (requests.Session()).post("https://technicaldebayan.net.in//Scripts/dir----oct-----110--!@/speedfollow", json=({"timer": 9, "cd": "follow", "usid": int(id.text), "auth": (auth.text), "submit": "submit"}),timeout=9999)
            print(get_ip.text)
        else:
            await e.answer('\n\n\n\nYou have access of me Contact @IshanSingle_xD', alert=True)

    elif e.data == b'FollowCheck':
        if e.chat.id in OWNERS:
            await e.answer('\nWelcome You Have Access of Me' )
            f = requests.Session()
            async with client.conversation(e.chat_id) as x:
                await x.send_message(f"Please Send You User Id")
                id = await x.get_response()
                await x.send_message(f"Please Send You Auth Token")
                auth = await x.get_response()
            auth="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJtV3NVWGhhUkZFeTFZTUU1dFNUQk5lbXNVWGhhUkYweVdYaFplbEUiLCJhdWQiOiJtV3NVWGhhUkZFeTFZTUU1dFNUQk5lbXNVWGhhUkYweVdYaFplbEUiLCJpYXQiOjE2NDM2NjI1MTksIm5iZiI6MTY0MzY2MjUxOSwiZGF0YSI6eyJ1c2VyX2lkIjoiNTUwNTQ2MjM2NiIsInRva2VuIjoiQWdPdHpMQkM1OGxzTk93S1hFcWtvdFo0QyJ9fQ.tiQTwFjiqrv66VacCjC-xhSYF2SMiTvy13kisj3bwwA"
            get_ip=f.post("https://technicaldebayan.net.in//Scripts/dir----oct-----110--!@/speedfollow", json=({"timer": 9, "cd": "follow", "usid": id, "auth": auth, "submit": "submit"}),timeout=1)
            print(get_ip.text)
        else:
            await e.answer('\n\n\n\nYou have access of me Contact @IshanSingle_xD', alert=True)



# <---------------- Telegram ---------------->
@client.on(events.CallbackQuery)
async def _(e):
    if e.data == b'Telegram':
        await e.answer('\nWelcome To Telegram Section')
        but=[
                [
                    Button.inline("Adding", b"Adding"),
                    Button.inline("FastAdding", b"FastAdding") 
                ],
                [
                    Button.inline("Stats", b"Stats"),
                    Button.inline("Edit", b"Edit")
                ],
                [
                    Button.inline("Back", b"Home"),
                ]
            ]
        await client.edit_message(e.chat.id, e.query.msg_id,f"**Welcome Sir!\n\nI'm Induced Members Bot \nMade for Adding Members\\Like\\Comments\\Vots\n\nMade with ❤️ By @InducedBots**", buttons=but)
    elif e.data == b"Adding":
        if e.chat.id in OWNERS:
            await e.answer('\nWelcome To Singla Adding')
            async with client.conversation(e.chat_id) as x:
                await x.send_message(f"Please Send Your Link")
                id = await x.get_response()
                await x.send_message(f"Please Send You Auth Token")
                auth = await x.get_response()
            i=id.text
            x=auth.text
            async def re():
                get_ip= (requests.Session()).post("https://smmworldpanel.com/api/v2", json=({"key": x, "action": "add", "service": 56, "link": i, "quantity":500}))
                red = json.loads(get_ip.text)
                if 'error' in red:
                    if red['error']=="You have active order with this link. Please wait until order being completed.":
                        await asyncio.sleep(5)
                        await re()
                    else:
                        await client.send_message(e.chat.id,f"Error:  `{red['error']}`\n\nToken: {x}\n\nMade with ❤️ By @InducedBots")
                        return
                else:
                    await client.send_message(e.chat.id,f"Order ID:  `{red['order']}`\nOrder Link: {i}\nOrder Token: `{x}`\n\nMade with ❤️ By @InducedBots")
                    if f"{e.query.user_id}" in Data:
                        Li=Data[f"{e.query.user_id}"]
                    else:
                        Li=[]
                    Li.append({"Id":red['order'],"Token":x})
                    Data[f"{e.query.user_id}"]=Li
                    if f"{e.chat.id}" in Data:
                        Li=Data[f"{e.chat.id}"]
                    else:
                        Li=[]
                    Li.append({"Id":red['order'],"Token":x})
                    Data[f"{e.chat.id}"]=Li
        else:
            await e.answer('\nYou Have No Access to me', alert=True)

    elif e.data == b"FastAdding":
        if e.chat.id in OWNERS:
            await e.answer('\nWelcome To Multiple Adding')
            async with client.conversation(e.chat_id) as x:
                await x.send_message(f"Please Send Your Link")
                id = await x.get_response()
                await x.send_message(f"Please Send You Auth Token")
                auth = await x.get_response()
            i=id.text
            x=auth.text
            while True:
                get_ip= (requests.Session()).post("https://smmworldpanel.com/api/v2", json=({"key": x, "action": "add", "service": 56, "link": i, "quantity":500}))
                red = json.loads(get_ip.text)
                if 'error' in red:
                    if red['error']=="You have active order with this link. Please wait until order being completed.":
                        await asyncio.sleep(5)
                    else:
                        await client.send_message(e.chat.id,f"Error:  `{red['error']}`\n\nToken: {x}\n\nMade with ❤️ By @InducedBots")
                        return
                else:
                    await client.send_message(e.chat.id,f"Order ID:  `{red['order']}`\nOrder Link: {i}\nOrder Token: `{x}`\n\nMade with ❤️ By @InducedBots")
                    if f"{e.query.user_id}" in Data:
                        Li=Data[f"{e.query.user_id}"]
                    else:
                        Li=[]
                    Li.append({"Id":red['order'],"Token":x})
                    Data[f"{e.query.user_id}"]=Li
                    if f"{e.chat.id}" in Data:
                        Li=Data[f"{e.chat.id}"]
                    else:
                        Li=[]
                    Li.append({"Id":red['order'],"Token":x})
                    Data[f"{e.chat.id}"]=Li
        else:
            await e.answer('\nYou Have No Access to me', alert=True)

    elif e.data == b"Stats":
        if e.chat.id in OWNERS:
            await e.answer('\nStats Checking Start')
            if f"{e.query.user_id}" in Data:
                await client.send_message(e.chat.id,"You have no Orders Till")
                return
            Li=[]
            for x in Data[f"{e.query.user_id}"]:
                get_ip= requests.get(f'https://smmworldpanel.com/api/v2?key={x["Token"]}apikey&action=status&order={x["Id"]}')
                red = json.loads(get_ip.text)
                if 'status' in red:
                    if red['status'] =="Canceled":
                        pass
                    else:
                        await e.reply(f"*✳Info Extracted*\n---------\n📦Order Status : {red['status']}\n🧾Remains : {red['remains']}\n\nMade with ❤️ By @InducedBots")
                        Li.append({"Id":x["Id"],"Token":x["Token"]})
                else:
                    await e.reply(f'Your Token May be revoked\nToken: {x["Token"]}\n\nMade with ❤️ By @InducedBots')
            Data[f"{e.query.user_id}"]=Li  



# <---------------- AdminPanel ---------------->
@client.on(events.CallbackQuery)
async def _(e):
    if e.data == b"Admin":
        if e.query.user_id == 1303790979:
            await e.answer('\nWelcome to Admin Pannel', alert=True)
            but=[
                    [
                        Button.inline("Stat", b"Stat"),
                        Button.inline("Restart", b"Restart") 
                    ],
                    [
                        Button.inline("Back", b"Home")
                    ]
                ]
            await client.edit_message(e.chat.id, e.query.msg_id,f"**Welcome Sir!\n\nI'm Induced Members Bot \nMade for Adding Members\\Like\\Comments\\Vots\n\nMade with ❤️ By @InducedBots**", buttons=but)
        else:
            await e.answer('\nYou Can not Access Admin Panel', alert=True)

    elif e.data == b"Stat":
        await e.answer('\nWait Checking Stats', alert=True)
        def time_formatter():
            minutes, seconds = divmod(int(time.time() - start_time), 60)
            hours, minutes = divmod(minutes, 60)
            days, hours = divmod(hours, 24)
            weeks, days = divmod(days, 7)
            tmp = (
                ((str(weeks) + "w: ") if weeks else "")
                + ((str(days) + "d: ") if days else "")
                + ((str(hours) + "h: ") if hours else "")
                + ((str(minutes) + "m: ") if minutes else "")
                + ((str(seconds) + "s") if seconds else "")
            )
            if tmp != "":
                if tmp.endswith(":"):
                    return tmp[:-1]
                else:
                    return tmp
            else:
                return "0 s"
        start = time.time()
        re=await e.client.send_message(e.chat.id,"Wait Checking Ping")
        end = round((time.time() - start) * 1000)
        uptime = time_formatter()
        R= psutil.virtual_memory().percent
        C= psutil.cpu_percent(interval=0.5)
        await re.edit(f"**Hey,  I am alive.\n┏━━━━━━━━━━━━━━━━━━━\n┣ Ping - `{end}ms`\n┣ UpTime - `{uptime}`\n┣ Ram - `{R} %`\n┣ Cpu - `{C} %`\n┗━━━━━━━━━━━━━━━━━━━\n\nMade with ❤️ By @InducedBots**") 

    elif e.data == b"Restart":
        await e.answer('\nRestarting Bot Wait', alert=True)
        os.execl(sys.executable, sys.executable, "-m", "main")

    elif e.data == b"Home":
        but=[
                [
                    Button.inline("Instagram", b"Instagram"),
                    Button.inline("Telegram", b"Telegram") 
                ],
                [
                    Button.url("Support ☎️", url=f"https://t.me/InducedBotsSupport"),
                    Button.inline("AdminPannel 🛰", b"Admin")
                ]
            ]
        await client.edit_message(e.chat.id, e.query.msg_id,f"**Welcome Sir!\n\nI'm Induced Members Bot \nMade for Adding Members\\Like\\Comments\\Vots\n\nMade with ❤️ By @InducedBots**", buttons=but)

@client.on(events.NewMessage(incoming=True, pattern='/check'))
async def _(e):
        if e.query.user_id == 1303790979:
            await e.answer('\nStats Checking Start')
            if f"{e.chat.id}" in Data:
                await client.send_message(e.chat.id,"You have no Orders Till")
                return
            Li=[]
            for x in Data[f"{e.chat.id}"]:
                get_ip= requests.get(f'https://smmworldpanel.com/api/v2?key={x["Token"]}apikey&action=status&order={x["Id"]}')
                red = json.loads(get_ip.text)
                if 'status' in red:
                    if red['status'] =="Canceled":
                        pass
                    else:
                        await e.reply(f"*✳Info Extracted*\n---------\n📦Order Status : {red['status']}\n🧾Remains : {red['remains']}\n\nMade with ❤️ By @InducedBots")
                        Li.append({"Id":x["Id"],"Token":x["Token"]})
                else:
                    await e.reply(f'Your Token May be revoked\nToken: {x["Token"]}\n\nMade with ❤️ By @InducedBots')
            Data[f"{e.chat.id}"]=Li 

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
            os.execl(sys.executable, sys.executable, "-m", "main")
else:
    try:
        client.run_until_disconnected()
    except:
        os.execl(sys.executable, sys.executable, "-m", "main")
