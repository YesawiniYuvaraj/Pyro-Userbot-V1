import sys
import io

from subprocess import getoutput as run
import traceback

import config, strings
import asyncio

from datetime import datetime
from pyrogram import filters, enums
from pyrogram.types import Message 
from Yuvaraj import bot, INFO , yuvaraj
from Yuvaraj.helpers.help_func import emoji_convert
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import MessageTooLong
from Yuvaraj import yuvaraj as app
async def aexec(code, app, msg):
    exec(
        "async def __aexec(app, msg): "
        + "\n p = print"
        + "".join(f"\n {l_}" for l_ in code.split("\n"))
    )
    return await locals()["__aexec"](app, msg)

@bot.on_message(filters.command("start") & filters.private)
async def start(_, message):
     user_id = message.from_user.id
     info = await INFO.yuvaraj()
     botlive = await emoji_convert(bot.is_connected)
     applive = await emoji_convert(yuvaraj.is_connected)
     name = info.first_name
     id = info.id
     if user_id in SPAM:
         return await message.reply("[`DON'T SPAM HERE`]")
     SPAM.append(user_id)
     await message.forward(config.GROUP_ID)
     mention = f"[{name}](tg://user?id={id})"
     BUTTON=InlineKeyboardMarkup([[
     InlineKeyboardButton("SOURCE 👾", url=config.SOURCE),]])
     await message.reply_text(text=strings.BOT_START.format(mention=mention, applive=applive, botlive=botlive),quote=True, reply_markup=BUTTON ,parse_mode=enums.ParseMode.MARKDOWN)
     await asyncio.sleep(20)
     SPAM.remove(user_id)
     return 
@bot.on_message(filters.command("run")& filters.user([6651534688]))
@bot.on_edited_message(filters.command("run")& filters.user)
async def runPyro_Funcs(app:app, msg:Message) -> None:
    code = msg.text.split(None, 1)
    if len(code) == 1:
        return await msg.reply("<sʏɴᴛᴀx ᴇʀʀᴏʀ> ᴄᴏᴅᴇ ɴᴏᴛ ғᴏᴜɴᴅ !")
    message = await msg.reply("ʀᴜɴɴɪɴɢ...")
    soac = datetime.now()
    osder = sys.stderr
    osdor = sys.stdout
    redr_opu = sys.stdout = io.StringIO()
    redr_err = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None
    try:
        vacue = await aexec(code[1], app, msg)
    except Exception:
        exc = traceback.format_exc()
    stdout = redr_opu.getvalue()
    stderr = redr_err.getvalue()
    sys.stdout = osdor
    sys.stderr = osder
    evason = exc or stderr or stdout or vacue or "ɴᴏ ᴏᴜᴛᴘᴜᴛ"
    eoac = datetime.now()
    runcs = (eoac - soac).microseconds / 1000
    oucode = f"📎 ᴄᴏᴅᴇ:\n<pre>{code[1]}</pre>\n📒 ᴏᴜᴛᴘᴜᴛ:\n<pre>{evason}</pre>\n✨ ᴛɪᴍᴇ ᴛᴀᴋᴇɴ: {runcs}ᴍɪʟɪsᴇᴄᴏɴᴅ"
    if len(oucode) > 4006:
        await message.edit("⚠️ ᴏᴜᴛᴘᴜᴛ ᴛᴏᴏ ʟᴏɴɢ...")
    else:
        await message.edit(oucode)
