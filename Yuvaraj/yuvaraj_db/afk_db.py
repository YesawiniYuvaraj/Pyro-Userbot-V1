from Yuvaraj import db
import asyncio

bd = db["afk"]

async def SET_AFK(time, reason):
    doc = {"_id": 1, "stats": True, "time": time, "reason": reason}
    try:
        await bd.insert_one(doc)
    except Exception:
        await bd.update_one({"_id": 1}, {"$set": {"stats": True, "time": time, "reason": reason}})
        
async def UNSET_AFK():
    await bd.update_one({"_id": 1}, {"$set": {"stats": False, "time": None, "reason": None}})
    
async def GET_AFK():
    Find = await bd.find_one({"_id": 1})
    if not Find:
        return False
    else:
        stats = Find["stats"]
        return stats

async def GET_AFK_TIME():
    Find = await bd.find_one({"_id": 1})
    if not Find:
        return False
    else:
        value = Find["time"]
        return value

async def GET_AFK_REASON():
    Find = await bd.find_one({"_id": 1})
    if not Find:
        return False
    else:
        value = Find["reason"]
        return value
