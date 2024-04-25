import pyrogram
import strings
import config

from Yuvaraj import bot , yuvaraj
from Yuvaraj.helpers.help_func import get_datetime 

async def run_clients():
      await bot.start()
      await yuvaraj.start()
      await pyrogram.idle()
      zone = await get_datetime()
      await bot.send_message(
           chat_id=config.GROUP_ID,
           text=strings.RESTART_TEXT1.format(date=zone["date"], time=zone["time"]))
      await barath.send_message(
           chat_id=config.GROUP_ID,
           text=strings.RESTART_TEXT2.format(date=zone["date"], time=zone["time"]))


if __name__ == "__main__":
    yuvaraj.loop.run_until_complete(run_clients())
