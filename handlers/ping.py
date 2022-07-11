import time
import os
import re
from main import lbda
from sys import argv
import platform
from datetime import datetime
from asyncio import sleep
from pyrogram import Client as sree
from pyrogram import filters
from pyrogram.types import Message
from pyrogram import __version__ as pyro
from cache.stuffs.string import (ptxt1, ptxt2)
from config import (BOT_NAME, OWNER_USERNAME, BOT_IMG)

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


@sree.on_message(filters.command("ping") & filters.group)
async def ping(sree, m: Message):
    pythn = platform.python_version()    
    start = datetime.now()
    start_time = time.time()
    b = await m.reply_photo(photo=BOT_IMG, caption=ptxt1)
    await sleep(1.5)
    end_time = time.time()
    uptime = get_readable_time((time.time() - lbda))
    pong1 = (datetime.now() - start).microseconds / 1000
    pong2 = str(round((end_time - start_time) * 1000, 3)) + " ms"
    await b.edit_text(ptxt2.format(BOT_NAME, pong1, pong2, uptime, pyro, pythn, OWNER_USERNAME))
    await sleep(0)
    await m.delete()
