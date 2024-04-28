from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Yuvaraj import yuvaraj as app
from config import HANDLER, OWNER_ID, YUVARAJ,SOURCE

@app.on_message(filters.command("help",prefixes=HANDLER) & filters.me)
async def help_command(client, message):
    await query.message.reply_text("Yuvaraj-UserBot Plugins\n"
    "+------------+------------+\n"
    "| Autopic    | admin      |\n"
    "| afk        | animation  |\n"
    "| anime_cf   | antipm     |\n"
    "| autoscroll | broadcast  |\n"
    "| carbon     | clone      |\n"
    "| create     | dictionary |\n"
    "| dmspam     | emoji      |\n"
    "| git        | globals    |\n"
    "| google     | info       |\n"
    "| invite     | joinleave  |\n"
    "| locks      | lyrics     |\n"
    "| memify     | mention    |\n"
    "| metrics    | music      |\n"
    "| paste      | pats       |\n"
    "| ping       | profile    |\n"
    "| purge      | quotly     |\n"
    "| raid       | replyraid  |\n"
    "| restart    | sangmata   |\n"
    "| screenshot | spam       |\n"
    "| start      | stats      |\n"
    "| sticker    | stickers   |\n"
    "| sudos      | tag        |\n"
    "| tagalert   | tagall     |\n"
    "| telegraph  | text       |\n"
    "| tiny       | unsplash   |\n"
    "| upload     | vctools    |\n"
    "| vulgar     | weather    |\n"
    "+------------+------------+\n")

