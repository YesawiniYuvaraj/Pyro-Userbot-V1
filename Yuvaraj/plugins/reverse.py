import os
from YUVARAJ import yuvaraj as app 
from pyrogram import *
from pyrogram.types import *
from datetime import datetime
from GoogleSearch import Search

@app.on_message(filters.command("pp") & filters.group, group=3)
async def pp(_,msg:Message):
    "reverse the image and send results"
    now = datetime.utcnow()
    if msg.reply_to_message and msg.reply_to_message.photo:
        ms = await msg.reply_text("wait for 2-3 second")
        X = await app.download_media(msg.reply_to_message,f"{now.microsecond}.jpg")
        sea = Search(X)
        await ms.edit_text(f"[{sea['output']}]({sea['similar']})")
        os.remove(f"./downloads/{now.microsecond}.jpg")
    else :
        await msg.reply("Reply to a image")
