import asyncio
import os
import re
import requests
from Yuvaraj import yuvaraj as app 
import aiofiles
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import HANDLER, OWNER_ID, YUVARAJ,SOURCE


pattern = re.compile(r"^text/|json$|yaml$|xml$|toml$|x-sh$|x-shellscript$")



async def neko_bin(content: str) -> str:
    url = "https://nekobin.com/api/documents"
    response = requests.post(
        url=url,
        headers={"Content-Type": "application/json"},
        json={"content": content},
    ).json()
    if response.get("ok"):
        return f"https://nekobin.com/{response.get('result').get('key')}"
    else:
        raise Exception("Failed to paste content to Nekobin")

@app.on_message(filters.command("paste" ,HANDLER) & filters.me)
async def paste_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text("Reply To A Message With .paste")
    m = await message.reply_text("Pasting...")
    if message.reply_to_message.text:
        content = str(message.reply_to_message.text)
    elif message.reply_to_message.document:
        document = message.reply_to_message.document
        if document.file_size > 1048576:
            return await m.edit("You can only paste files smaller than 1MB.")
        if not pattern.search(document.mime_type):
            return await m.edit("Only text files can be pasted.")
        doc = await message.reply_to_message.download()
        async with aiofiles.open(doc, mode="r") as f:
            content = await f.read()
        os.remove(doc)

    try:
        nekobin_url = await neko_bin(content)

        if nekobin_url:
            output = f"ʜᴇʀᴇ ɪꜱ ʏᴏᴜʀ ᴘᴀꜱᴛᴇ ʟɪɴᴋ:\n\n❂ 𝗡𝗲𝗸𝗼𝗕𝗶𝗻\n"


        await message.reply(output,
disable_web_page_preview=True
)
    except Exception as e:
        await message.reply(f"Error: {e}", quote=False)

    await m.delete()
