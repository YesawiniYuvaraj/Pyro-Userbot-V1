import uuid
from pyrogram import Client, filters
from pyrogram.types import (InlineKeyboardMarkup, InlineKeyboardButton, Message)
import httpx
from Yuvaraj import yuvaraj as app

COMMANDS = ['reverse', 'grs', 'pp']

@app.on_message(filters.command(COMMANDS))
async def on_reverse(client: Client, message: Message) -> Message:
    if not message.reply_to_message or not message.reply_to_message.media:
        await message.reply(STRINGS.REPLY_TO_MEDIA)
        return
    media_type = message.reply_to_message.media
    if media_type not in ('photo', 'sticker', 'document'):
        if media_type == 'animation':
            await message.reply(STRINGS.GIF_NOT_SUPPORTED)
            return
        await message.reply(STRINGS.THESE_MEDIA_TYPES_ONLY)
        return
    status_msg = await message.reply(STRINGS.DOWNLOADING_MEDIA)
    file_path = f'downloads/{uuid.uuid4()}'
    await message.reply_to_message.download(file_path)
    await status_msg.edit(STRINGS.UPLOADING_MEDIA)
    async with httpx.AsyncClient(timeout=30) as async_client:
        with open(file_path, 'rb') as file:
            files = {'file': file}
            response = await async_client.post(API_URL, files=files)
        response_json = response.json()
        if response.status_code != 200:
            await message.reply(STRINGS.API_ERROR.format(response_json['error']) + STRINGS.SUPPORT_CHAT)
            return
        search_keyword = response_json['keyword']
        url = response_json['url']
    text = STRINGS.REVERSE_RESULT.format(search_keyword, url)
    reply_markup = [
        [InlineKeyboardButton('Open Link', url=url)]
        ]
    await message.reply(text, reply_markup=InlineKeyboardMarkup(reply_markup))
    await status_msg.delete()
