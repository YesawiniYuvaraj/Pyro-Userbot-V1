import pyrogram
import strings
import config

from Yuvaraj import bot , yuvaraj
from Yuvaraj.helpers.help_func import get_datetime 
from Yuvaraj.web import keep_alive, web_server
from aiohttp import web
import logging, os, random
import asyncio
from Yuvaraj import yuvaraj as bot

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

log = logging.getLogger(__name__)

PORT = int(os.environ.get("PORT", 8080))
BIND_ADDRESS = str(os.environ.get("WEB_SERVER_BIND_ADDRESS", "0.0.0.0"))


async def start_services():        
        server = web.AppRunner(web_server())
        await server.setup()
        await web.TCPSite(server, BIND_ADDRESS, PORT).start()
        log.info("Web Server Initialized Successfully")
        log.info("=========== Service Startup Complete ===========")
  
        asyncio.create_task(keep_alive())
        log.info("Keep Alive Service Started")
        log.info("=========== Initializing Web Server ===========")
        


if __name__ == "__main__":
     loop = asyncio.get_event_loop()
     loop.run_until_complete(start_services())
     bot.run()
     log.info('Bot Started!')
