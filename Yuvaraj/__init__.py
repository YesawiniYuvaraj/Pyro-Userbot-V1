import os
import time
import logging
from pyrogram import Client
from pymongo import MongoClient
import motor.motor_asyncio

FORMAT = "[Yuvaraj]: %(message)s"

logging.basicConfig(level=logging.INFO, handlers=[logging.FileHandler('logs.txt'),
                                                    logging.StreamHandler()], format=FORMAT)

StartTime = time.time()

MODULE = []

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time


# Set up logging
logger = logging.getLogger(__name__)

# Set up database connection
DB_URL = os.getenv("DB_URL","mongodb+srv://publicDB:publicDBbyKira@public.twckcqf.mongodb.net/?retryWrites=true&w=majority")



# Set up bot configurations
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
SESSION = os.getenv("SESSION")
TOKEN = os.getenv("TOKEN")
DB_NAME = os.getenv("DB_NAME","PyroX-UB")

cli = motor.motor_asyncio.AsyncIOMotorClient(DB_URL)
db=cli[DB_NAME]

DB = MongoClient(DB_URL)
DATABASE = DB[DB_NAME]

# PYROGRAM USER CLIENT 
yuvaraj = Client(name="Yuvaraj", session_string=SESSION, api_id=API_ID, api_hash=API_HASH, plugins=dict(root="Yuvaraj"))

#PYROGRAM BOT CLIENT
bot = Client(name="YuvarajBot", bot_token=TOKEN, api_id=API_ID, api_hash=API_HASH, plugins=dict(root="Yuvaraj"))



class INFO:
   def barath():
      info = barath.get_me()
      return info   
     
   def bot():
      info = bot.get_me()
      return info
   
