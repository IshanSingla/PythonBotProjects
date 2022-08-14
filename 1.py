import asyncio
from telegraph import upload_file
from firebase_admin import credentials, db
from datetime import datetime, date
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
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
}
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
sent, bad_proxy, done, next_proxy = 0, 0, 0, 0


def send_views():
    global sent, bad_proxy, done, next_proxy
    while True:
        try:
            proxy = proxies[next_proxy]
            next_proxy += 1
        except IndexError:
            break
        try:
            _headers = {
                'accept-language': 'en-US,en;q=0.9',
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36',
                'x-requested-with': 'XMLHttpRequest'
            }
            session = requests.session()
            session.proxies.update({'http': f'http://{proxy}', 'https': f'http://{proxy}'})
            session.headers.update(_headers)
            main_res = session.get( f'https://t.me/InducedBots/2?embed=1').text
            _token = re.search('data-view="([^"]+)', main_res).group(1)
            views_req = session.get('https://t.me/v/?views=' + _token)
            with open('proxy.txt', 'a+') as good:
                good.write(proxy+'\n')
            sent += 1
            done += 1
            print(
                f"Stats : {done}\n---- Sent : {sent} Views\n---- Bad proxies : {bad_proxy}\n")

        except requests.exceptions.ConnectionError:
            # print('\033[1;31m❌ Bad Proxy\033[1;31m')
            bad_proxy += 1
            done += 1


# @client.on(telethon.events.NewMessage(incoming=True, pattern='/relode', func=lambda e: e.is_private))
async def _():
    global proxies
    for ux in links:
        res = requests.get(ux, headers=headers)
        proxie = re.findall(
            r'\d\d?\d?\.\d\d?\d?\.\d\d?\d?\.\d\d?\d?:\d\d\d?\d?\d?', res.text)
        for x in proxie:
            proxies.append(x)
    proxies = list(set(proxies))
    proxies.sort()
    Threads = []
    for t in range(500):
        x = threading.Thread(target=send_views)
        x.start()
        Threads.append(x)

    for Th in Threads:
        Th.join()

loop = asyncio.get_event_loop()
loop.run_until_complete(_())
