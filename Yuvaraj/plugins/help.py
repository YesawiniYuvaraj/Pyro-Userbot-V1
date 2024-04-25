from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Yuvaraj import yuvaraj as app
from config import HANDLER, OWNER_ID, YUVARAJ,SOURCE

@app.on_message(filters.command("help", prefixes=HANDLER) & filters.me)
async def help_command(client, message):
    await query.message.reply_photo(
        photo="https://graph.org/file/ce692dfc420ddb469fa0b.jpg",
        caption="Userbots Command",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Plugins", callback_data="plug"),
                    InlineKeyboardButton("Bot", callback_data="bot")
                ]
            ]
        )
    )

@app.on_callback_query()
async def callback_handler(client, query):
    if query.data == "plug":
       
        await query.message.edit_reply_markup(
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Alive", callback_data="al"),
                        InlineKeyboardButton("Ping", callback_data="ping")
                    ]
                ]
            )
        )
    elif query.data == "al":
       
        await query.message.edit_text("Use /alive")
    elif query.data == "ping":
         await query.message.edit_text("Use /ping")
