from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Yuvaraj import yuvaraj as app
from config import HANDLER, OWNER_ID, YUVARAJ,SOURCE

@app.on_message(filters.command("help",prefixes=HANDLER) & filters.me)
async def help_command(client, message):
    plugins_list = """
Yuvaraj-UserBot Plugins
+------------+------------+
| Autopic    | admin      |
| afk        | animation  |
| anime_cf   | antipm     |
| autoscroll | broadcast  |
| carbon     | clone      |
| create     | dictionary |
| dmspam     | emoji      |
| git        | globals    |
| google     | info       |
| invite     | joinleave  |
| locks      | lyrics     |
| memify     | mention    |
| metrics    | music      |
| paste      | pats       |
| ping       | profile    |
| purge      | quotly     |
| raid       | replyraid  |
| restart    | sangmata   |
| screenshot | spam       |
| start      | stats      |
| sticker    | stickers   |
| sudos      | tag        |
| tagalert   | tagall     |
| telegraph  | text       |
| tiny       | unsplash   |
| upload     | vctools    |
| vulgar     | weather    |
+------------+------------+
"""
async def my_function():
    await query.message.reply_text(plugins_list, quote=True)
