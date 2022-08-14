import asyncio
import sys
import telethon
import os
import time
import psutil
import shutil

api_id = 2681714
api_hash = "48059e206028f3d626d0fe569701cf45"
chat = (os.getenv('chats', "inducedview Cricket_Match_IPL_Prediction")).split()
start_time = time.time()
acc = []
client = telethon.TelegramClient(None, api_id, api_hash).start(
    bot_token="5286961271:AAG40BkIaOL5ZjsHhUCsB-LswX02Al27UAs")


async def login():
    global acc
    for r in os.listdir(f'sessions'):
        if not r.endswith(".session"):
            continue
        r = r.replace('.session', '')
        try:
            cl = telethon.TelegramClient(f"sessions/{r}", api_id, api_hash)
            await cl.connect()
            k = (await cl.get_me()).first_name
            acc.append(cl)
            await client.send_message(1303790979, f"{len(acc)}) Account {k} is online")
            for chats in chat:
                try:
                    await cl(telethon.functions.channels.JoinChannelRequest(chats))
                except:
                    pass
        except:
            await cl.disconnect()
            pass
    await client.send_message(1303790979, f" Total {len(acc)} Account are online")

loop = asyncio.get_event_loop()
loop.run_until_complete(login())


@client.on(telethon.events.NewMessage(incoming=True, pattern='/start', func=lambda e: e.is_private))
async def _(e):
    start = time.time()
    ss = await client.send_message(e.chat.id, "Checking Stats", buttons=[[telethon.Button.inline("📊 Staus", b"Stat"), ]])
    end = round((time.time() - start) * 1000)

    def humanbytes(size):

        if size in [None, ""]:
            return "0 B"
        for unit in ["B", "KB", "MB", "GB"]:
            if size < 1024:
                break
            size /= 1024
        return f"{size:.2f} {unit}"

    def time_formatter():
        minutes, seconds = divmod(int(time.time() - start_time), 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        weeks, days = divmod(days, 7)
        tmp = (
            ((str(weeks) + "w:") if weeks else "")
            + ((str(days) + "d:") if days else "")
            + ((str(hours) + "h:") if hours else "")
            + ((str(minutes) + "m:") if minutes else "")
            + ((str(seconds) + "s") if seconds else "")
        )
        if tmp != "":
            if tmp.endswith(":"):
                return tmp[:-1]
            else:
                return tmp
        else:
            return "0 s"
    total, used, free = shutil.disk_usage(".")
    cpuUsage = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    upload = humanbytes(psutil.net_io_counters().bytes_sent)
    down = humanbytes(psutil.net_io_counters().bytes_recv)
    TOTAL = humanbytes(total)
    USED = humanbytes(used)
    FREE = humanbytes(free)
    tex = f"Total Details\n\nBot Usage:\n┏━━━━━━━━━━━━━━━━\n┣Ping - `{end}ms`\n┣UpTime - `{time_formatter()}`\n┗━━━━━━━━━━━━━━━━\n\nSystem Usage:\n┏━━━━━━━━━━━━━━━━\n┣UplodeSpeed: {upload}\n┣Download: {down}\n┣Cpu: {cpuUsage}%\n┣Ram: {memory}%\n┃\n┣Storage Used: {disk}%\n┃┏━━━━━━━━━━━━━━━━\n┃┣Total: {TOTAL}\n┃┣Used: {USED}\n┃┣Free: {FREE}\n┃┗━━━━━━━━━━━━━━━━\n┗━━━━━━━━━━━━━━━━\n\nMade With ❤️ By @InducedBots"
    await ss.edit(tex)


@client.on(telethon.events.NewMessage(incoming=True, pattern='/sudo', func=lambda e: e.is_private))
async def _(e):
    async with client.conversation(e.chat_id) as xmr:
        if e.chat.id == 1303790979:
            await xmr.send_message("Send Username ")
            try:
                Zip = await xmr.get_response(timeout=300)
                if Zip.text == "/start" or Zip.text == "/help":
                    return
                chat.append(Zip.text)
                await xmr.send_message(f"{Zip.text} Set Sucessfully")
            except:
                pass


@client.on(telethon.events.NewMessage(incoming=True, chats=chat))
async def _(e):
    done = 0
    error = 0
    kk = await client.send_message(1303790979, f"Views Start Sucessfully\n\nDone: {done}\nFailed: {error}\nTotal: {done+error}\n\nMade With ❤️ By @InducedBots")
    idse = (await client.get_entity(e.peer_id.channel_id)).username
    for x in acc:
        try:
            await x(telethon.functions.messages.GetMessagesViewsRequest(
                peer=f"{idse}",
                id=[e.id],
                increment=True
            ))
            done += 1
        except:
            error += 1
    await kk.edit(f"Broadcast Sucessfully\n\nDone: {done}\nFailed: {error}\nTotal: {done+error}\n\nMade With ❤️ By @InducedBots")


# @client.on(telethon.events.NewMessage(incoming=True, chats=chat))
# async def _(e):
#     done = 0
#     error = 0
#     kk = await client.send_message(1303790979, f"Views Start Sucessfully\n\nDone: {done}\nFailed: {error}\nTotal: {done+error}\n\nMade With ❤️ By @InducedBots")
#     for r in os.listdir(f'sessions'):
#         if not r.endswith(".session"):
#             continue
#         r = r.replace('.session', '')
#         try:
#             cl = telethon.TelegramClient(f"sessions/{r}", api_id, api_hash)
#             await cl.connect()
#             k = (await cl.get_me()).first_name
#             idse = (await client.get_entity(e.peer_id.channel_id)).username
#             await cl(telethon.functions.channels.JoinChannelRequest(idse))
#             await cl(telethon.functions.messages.GetMessagesViewsRequest(
#                 peer=f"{idse}",
#                 id=[e.id],
#                 increment=True
#             ))
#             done += 1
#             await cl.disconnect()
#             # await asyncio.sleep(random.choice(range(10, 20)))
#         except:
#             try:
#                 await cl.disconnect()
#             except:
#                 pass
#             error += 1
#     await kk.edit(f"Broadcast Sucessfully\n\nDone: {done}\nFailed: {error}\nTotal: {done+error}\n\nMade With ❤️ By @")


text = """
┏━━┓      ┏┓              ┏┓    ┏━━┓        ┏━━━┓    ┏┓           
┗┫┣┛      ┃┃              ┃┃    ┗┫┣┛        ┃┏━┓┃    ┃┃           
 ┃┃ ┏━┓ ┏━┛┃┏┓┏┓┏━━┓┏━━┓┏━┛┃     ┃┃ ┏━━┓    ┃┃ ┃┃┏━┓ ┃┃ ┏┓┏━┓ ┏━━┓
 ┃┃ ┃┏┓┓┃┏┓┃┃┃┃┃┃┏━┛┃┏┓┃┃┏┓┃     ┃┃ ┃━━┫    ┃┃ ┃┃┃┏┓┓┃┃ ┣┫┃┏┓┓┃┏┓┃
┏┫┣┓┃┃┃┃┃┗┛┃┃┗┛┃┃┗━┓┃┃━┫┃┗┛┃    ┏┫┣┓┣━━┃    ┃┗━┛┃┃┃┃┃┃┗┓┃┃┃┃┃┃┃┃━┫
┗━━┛┗┛┗┛┗━━┛┗━━┛┗━━┛┗━━┛┗━━┛    ┗━━┛┗━━┛    ┗━━━┛┗┛┗┛┗━┛┗┛┗┛┗┛┗━━┛
Induced Views Started Sucessfully........
"""
print(text)
try:
   client.run_until_disconnected()
   for xr in acc:
      xr.run_until_disconnected()
except:
   os.execl(sys.executable, sys.executable, "-m", "main")
