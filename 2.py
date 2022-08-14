import asyncio
import sys
import telethon
import random
import os
import time
import psutil
import threading
import telethon
import re
import requests

text = """
 ---------------------------------
     ╔════╗
     ╚═╗╔═╝
     ╔═╣╠═╗
     ║╔╣╠╗║
     ║╚╣╠╝║
     ╚═╣╠═╝
     ╔═╝╚═╗
     ╚════╝
 ---------------------------------
 """
with open("log.txt", "w") as f:
    f.write(text)

proxies = []
links = [
    "https://www.proxy-list.download/api/v1/get?type=http",
    "https://www.proxy-list.download/api/v1/get?type=https",
    "https://www.proxy-list.download/api/v1/get?type=socks4",
    "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http",
    "https://openproxy.space/list/socks4",
    "https://openproxy.space/list/http",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
    "https://raw.githubusercontent.com/User-R3X/proxy-list/main/online/socks4.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
    "https://raw.githubusercontent.com/almroot/proxylist/master/list.txt",
    "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
    "https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http%2Bhttps.txt",
    "https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
    "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
    "https://raw.githubusercontent.com/User-R3X/proxy-list/main/online/http%2Bs.txt",
    "https://raw.githubusercontent.com/Volodichev/proxy-list/main/http.txt",
]
links = list(set(links))
api_id = 2681714
api_hash = "48059e206028f3d626d0fe569701cf45"
chat = (os.getenv('chat', "inducedview Fixerkabaphu")).split()
start_time = time.time()

client = telethon.TelegramClient(None, api_id, api_hash).start(
    bot_token="5286961271:AAG40BkIaOL5ZjsHhUCsB-LswX02Al27UAs")
client1 = telethon.TelegramClient(None, api_id, api_hash).start(
    bot_token="5286961271:AAG40BkIaOL5ZjsHhUCsB-LswX02Al27UAs")
client2 = telethon.TelegramClient(None, api_id, api_hash).start(
    bot_token="5286961271:AAG40BkIaOL5ZjsHhUCsB-LswX02Al27UAs")
client3 = telethon.TelegramClient(None, api_id, api_hash).start(
    bot_token="5286961271:AAG40BkIaOL5ZjsHhUCsB-LswX02Al27UAs")
client4 = telethon.TelegramClient(None, api_id, api_hash).start(
    bot_token="5286961271:AAG40BkIaOL5ZjsHhUCsB-LswX02Al27UAs")
client5 = telethon.TelegramClient(None, api_id, api_hash).start(
    bot_token="5286961271:AAG40BkIaOL5ZjsHhUCsB-LswX02Al27UAs")
client6 = telethon.TelegramClient(None, api_id, api_hash).start(
    bot_token="5286961271:AAG40BkIaOL5ZjsHhUCsB-LswX02Al27UAs")
client7 = telethon.TelegramClient(None, api_id, api_hash).start(
    bot_token="5286961271:AAG40BkIaOL5ZjsHhUCsB-LswX02Al27UAs")
client8 = telethon.TelegramClient(None, api_id, api_hash).start(
    bot_token="5286961271:AAG40BkIaOL5ZjsHhUCsB-LswX02Al27UAs")
client9 = telethon.TelegramClient(None, api_id, api_hash).start(
    bot_token="5286961271:AAG40BkIaOL5ZjsHhUCsB-LswX02Al27UAs")


@client.on(telethon.events.NewMessage(incoming=True, pattern='/start', func=lambda e: e.is_private))
async def _(e):
    start = time.time()
    ss = await client.send_message(e.chat.id, "Checking Stats", buttons=[[telethon.Button.inline("📊 Staus", b"Stat"), ]])
    end = round((time.time() - start) * 1000)

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
    cpuUsage = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent

    tex = f"Total Details\n\nBot Usage:\n┏━━━━━━━━━━━━━━━━\n┣Ping - `{end}ms`\n┣UpTime - `{time_formatter()}`\n┗━━━━━━━━━━━━━━━━\n\nSystem Usage:\n┏━━━━━━━━━━━━━━━━\n┣Cpu: {cpuUsage}%\n┣Ram: {memory}%\n┃┗━━━━━━━━━━━━━━━━\n\nMade With ❤️ By @InducedBots"
    await ss.edit(tex)

@client9.on(telethon.events.NewMessage(incoming=True, chats=chat))
@client8.on(telethon.events.NewMessage(incoming=True, chats=chat))
@client7.on(telethon.events.NewMessage(incoming=True, chats=chat))
@client6.on(telethon.events.NewMessage(incoming=True, chats=chat))
@client5.on(telethon.events.NewMessage(incoming=True, chats=chat))
@client4.on(telethon.events.NewMessage(incoming=True, chats=chat))
@client3.on(telethon.events.NewMessage(incoming=True, chats=chat))
@client2.on(telethon.events.NewMessage(incoming=True, chats=chat))
@client1.on(telethon.events.NewMessage(incoming=True, chats=chat))
@client.on(telethon.events.NewMessage(incoming=True, chats=chat))
async def _(e):
    proxies.sort()
    kk = await e.client.send_message(1303790979, f"Views Start Sucessfully")
    idse = (await e.client.get_entity(e.peer_id.channel_id)).username
    _headers = {
        'accept-language': 'en-US,en;q=0.9',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }
    for x in range(0, 2000):
        try:
            proxy = proxies[random.randint(0, len(proxies))]
            session = requests.session()
            session.proxies.update(
                {'http': f'http://{proxy}', 'https': f'http://{proxy}'})
            session.headers.update(_headers)
            main_res = session.get(f'https://t.me/{idse}/{e.id}?embed=1').text
            _token = re.search('data-view="([^"]+)', main_res).group(1)
            views_req = session.get('https://t.me/v/?views=' + _token)
            print("done")
        except:
            pass
    await kk.edit(f"Views Added Sucessfully\n\nMade With ❤️ By @InducedBots")


async def _():
    global proxies
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    }
    while True:
        proxies = []
        for ux in links:
            res = requests.get(ux, headers=headers)
            proxie = re.findall(
                r'\d\d?\d?\.\d\d?\d?\.\d\d?\d?\.\d\d?\d?:\d\d\d?\d?\d?', res.text)
            for x in proxie:
                proxies.append(x)
        proxies = list(set(proxies))
        proxies.sort()
        print(len(proxies))
        await asyncio.sleep(60*60)

loop = asyncio.get_event_loop()
loop.run_until_complete(_())


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
except:
    os.execl(sys.executable, sys.executable, "-m", "main")
