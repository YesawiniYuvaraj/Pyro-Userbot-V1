from pyrogram import filters
import asyncio
from pyrogram import client
from Yuvaraj import yuvaraj
from Yuvaraj.helpers.help_func import get_arg
import Yuvaraj.yuvaraj_db.afk_db as Zect
from Yuvaraj.helpers.help_func import user_afk
from Yuvaraj import get_readable_time
from Yuvaraj.helpers.utils import get_message_type, Types
from config import HANDLER, OWNER_ID, GROUP_ID
from Yuvaraj.helpers.help_func import get_datetime 
import time


MENTIONED = []
AFK_RESTIRECT = {}
DELAY_TIME = 20


@yuvaraj.on_message(filters.command("afk", HANDLER) & filters.me)
async def afk(yuvaraj, message):
    afk_time = int(time.time())
    arg = get_arg(message)
    if not arg:
        reason = None
    else:
        reason = arg
    await Zect.set_afk(True, afk_time, reason)
    await message.edit("**I'm goin' AFK**")


@yuvaraj.on_message(filters.mentioned & ~filters.bot & filters.create(user_afk), group=11)
async def afk_mentioned(_, message):
    global MENTIONED
    afk_time, reason = await Zect.afk_stuff()
    afk_since = get_readable_time(time.time() - afk_time)
    if "-" in str(message.chat.id):
        cid = str(message.chat.id)[4:]
    else:
        cid = str(message.chat.id)

    if cid in list(AFK_RESTIRECT) and int(AFK_RESTIRECT[cid]) >= int(time.time()):
        return
    AFK_RESTIRECT[cid] = int(time.time()) + DELAY_TIME
    if reason:
       await message.reply(
        f"**I'm AFK right now (since {afk_since})\nReason:** __{reason}__"
        )
    else:
        await message.reply(f"**I'm AFK right now (since {afk_since})**")

        _, message_type = get_message_type(message)
        if message_type == Types.TEXT:
            text = message.text or message.caption
        else:
            text = message_type.name

        MENTIONED.append(
            {
                "user": message.from_user.first_name,
                "user_id": message.from_user.id,
                "chat": message.chat.title,
                "chat_id": cid,
                "text": text,
                "message_id": message.message_id,
            }
        )


@yuvaraj.on_message(filters.create(user_afk) & filters.outgoing)
async def auto_unafk(_, message):
    await Zect.set_unafk()
    unafk_message = await barath.send_message(message.chat.id, "**I'm no longer AFK**")
    global MENTIONED
    text = "**Total {} mentioned you**\n".format(len(MENTIONED))
    for x in MENTIONED:
        msg_text = x["text"]
        if len(msg_text) >= 11:
            msg_text = "{}...".format(x["text"])
        text += "- [{}](https://t.me/c/{}/{}) ({}): {}\n".format(
            x["user"],
            x["chat_id"],
            x["message_id"],
            x["chat"],
            msg_text,
        )
        await yuvaraj.send_message(GROUP_ID, text)
        MENTIONED = []
    await asyncio.sleep(2)
    await unafk_message.delete()
