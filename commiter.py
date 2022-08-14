import datetime
import os
import re
import time
import requests

while True:
    try:
        links = [
            "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
            "https://raw.githubusercontent.com/almroot/proxylist/master/list.txt",
            "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
            "https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt",
            "https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt",
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http%2Bhttps.txt",
        ]
        http=[
            "https://raw.githubusercontent.com/Volodichev/proxy-list/main/http.txt",
            "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
        ]
        https=[
            "https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt",
            "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
            "https://raw.githubusercontent.com/User-R3X/proxy-list/main/online/http%2Bs.txt",
        ]
        socks4=[
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt",
            "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt",
            "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
            "https://raw.githubusercontent.com/User-R3X/proxy-list/main/online/socks4.txt",
        ]
        socks4proxies=[]
        proxies=[]
        httpproxies=[]
        httpsproxies=[]

        for ux in links:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
            }
            res = requests.get(ux, headers=headers)
            proxie = re.findall(r'\d\d?\d?\.\d\d?\d?\.\d\d?\d?\.\d\d?\d?:\d\d\d?\d?\d?', res.text)
            for x in proxie:
                proxies.append(x)
        proxies = list(set(proxies))

        for ux in http:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
            }
            res = requests.get(ux, headers=headers)
            httpproxie = re.findall(r'\d\d?\d?\.\d\d?\d?\.\d\d?\d?\.\d\d?\d?:\d\d\d?\d?\d?', res.text)
            for x in httpproxie:
                httpproxies.append(x)
        httpproxies = list(set(httpproxies))

        for ux in https:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
            }
            res = requests.get(ux, headers=headers)
            httpsproxie = re.findall(r'\d\d?\d?\.\d\d?\d?\.\d\d?\d?\.\d\d?\d?:\d\d\d?\d?\d?', res.text)
            for x in httpsproxie:
                httpsproxies.append(x)
        httpsproxies = list(set(httpsproxies))

        for ux in socks4:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
            }
            res = requests.get(ux, headers=headers)
            socks4proxie = re.findall(r'\d\d?\d?\.\d\d?\d?\.\d\d?\d?\.\d\d?\d?:\d\d\d?\d?\d?', res.text)
            for x in socks4proxie:
                socks4proxies.append(x)
        socks4proxies = list(set(socks4proxies))
        try:
            os.chdir("proxy-list")
        except:
            pass
        with open("proxys/http.txt", "w") as f:
            f.write('\n'.join(httpproxies))
        with open("proxys/https.txt", "w") as f:
            f.write('\n'.join(httpsproxies))
        with open("proxys/proxys.txt", "w") as f:
            f.write('\n'.join(proxies))
        with open("proxys/socks4.txt", "w") as f:
            f.write('\n'.join(socks4proxies))
        os.system("git add .")
        os.system(f"git commit -m \'Proxys Update {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\'")
        os.system("git push origin main")
        os.chdir("../")
        
    except Exception as e:
        print(e)
        pass
    time.sleep(600)
