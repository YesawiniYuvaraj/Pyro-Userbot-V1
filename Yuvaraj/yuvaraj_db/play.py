from Yuvaraj import db
import asyncio
import random
import logging

d = db["playgroups"]

class play:
    async def get(self):
        try:
            info = await d.find_one({"_id": 1})
            if info and 'chats' in info:
                return info['chats'] or []
            return []
        except Exception as e:
            logging.error(e)
            return str(e)
    async def addRemove(self, chat_id, addOrRemove='add'):
        try:
            if addOrRemove == 'add':
                info = await d.find_one({"_id": 1}) or []
                if 'chats' in info and chat_id in info['chats']:
                    return 'ALREADY'
                await d.update_one({"_id": 1}, {"$addToSet": {"chats": int(chat_id)}}, upsert=True)
                return "SUCCESS"
            elif addOrRemove == 'remove':
                info = await d.find_one({"_id": 1}) or []
                if 'chats' in info and chat_id in info['chats']:
                    await db.update_one({"_id": 1}, {"$pull": {"chats": int(chat_id)}})
                    return "SUCCESS"
                else: return 'ALREADY'
            else:
                return "Invalid operation"
        except Exception as e:
            logging.error(e)
            return str(e)
