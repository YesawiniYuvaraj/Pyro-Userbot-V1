import logging
import asyncio
from Yuvaraj import yuvaraj as bot
from Yuvaraj.helpers.help_func import get_datetime
from Yuvaraj.web import keep_alive, web_server
from aiohttp import web

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

log = logging.getLogger(__name__)

async def run_clients():
    try:
        logging.info("Starting the bot...")
        await bot.start()
        await yuvaraj.start()
        logging.info("Both clients started successfully.")

        zone = await get_datetime()
        await bot.send_message(
            chat_id=config.GROUP_ID,
            text=strings.RESTART_TEXT1.format(date=zone["date"], time=zone["time"])
        )
        await yuvaraj.send_message(
            chat_id=config.GROUP_ID,
            text=strings.RESTART_TEXT2.format(date=zone["date"], time=zone["time"])
        )

        await asyncio.sleep(5)  # Simulate some additional startup tasks
        logging.info("Bot is now idling.")
        await pyrogram.idle()
    except Exception as e:
        logging.error(f"An error occurred: {e}")

async def start_services():
    server = web.AppRunner(web_server())
    await server.setup()
    await web.TCPSite(server, "0.0.0.0", 8080).start()
    logging.info("Web server initialized successfully.")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(start_services())
        loop.run_until_complete(run_clients())
