from pyrogram import Client, filters
import requests
from Yuvaraj import yuvaraj as app 
from config import HANDLER, OWNER_ID, YUVARAJ,SOURCE

def send_typing_action(client, chat_id):
    app.send_chat_action(chat_id, "typing")

def get_answer(message):
    url = "https://chatgpt.apinepdev.workers.dev/?question=" + message
    response = requests.get(url)
    data = response.json()
    return data.get("answer")

@app.on_message(filters.command('ask', HANDLER) & filters.me)
async def handle_message(client, message):
    send_typing_action(client, message.chat.id)
    answer = get_answer(message.text)
    if not answer:
        send_typing_action(client, message.chat.id)
        await message.reply_text("❌ Something Went Wrong.")
        return
    send_typing_action(client, message.chat.id)
    await message.reply_text(answer)
