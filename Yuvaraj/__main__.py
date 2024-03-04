import pyrogram
import asyncio
import strings
import config

from Yuvaraj import bot , yuvaraj, LOGGER
from Yuvaraj.helpers.help_func import get_datetime 

async def run_clients():
      zone = await get_datetime()
      try:
          await bot.start()
          await yuvaraj.start()
          await bot.send_message(
              chat_id=config.GROUP_ID,
              text=strings.RESTART_TEXT1.format(date=zone["date"], time=zone["time"]))
          await barath.send_message(
              chat_id=config.GROUP_ID,
              text=strings.RESTART_TEXT2.format(date=zone["date"], time=zone["time"]))
      except Exception as e:
          LOGGER.info(e)  
      await pyrogram.idle()
   
if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(run_clients()
