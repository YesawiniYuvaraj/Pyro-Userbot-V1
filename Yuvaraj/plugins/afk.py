from pyrogram import filters
from Yuvaraj import yuvaraj
from config import HANDLER, OWNER_ID, GROUP_ID
from Restart import restart_program
import os
import re
from datetime import datetime
from Yuvaraj.yuvaraj_db.afk_db import SET_AFK, UNSET_AFK, GET_AFK_TIME, GET_AFK_REASON

# Option to allow bots to bypass AFK
BOTS_ALLOWED_TO_WORK_IN_BUSY_COMMANDS = False

# Function to calculate time difference in human-readable format
def calculate_time(start_time, end_time):
    uptime = (end_time - start_time).total_seconds()
    hours, remainder = divmod(uptime, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{int(hours)}h {int(minutes)}m {int(seconds)}s"

# Function to remove AFK status when the user sends a message
async def afk_remove(_, client, update):
    if await GET_AFK():  # Check if the user is in AFK mode
        Busy_time = await GET_AFK_TIME()  # Get the time AFK was set
        formatted_elapsed_time = calculate_time(Busy_time, datetime.now())
        await UNSET_AFK()  # Unset AFK status
        await update.reply_text(
            f"➲ **Hello**, Master Welcome Again ✨🥀.\n"
            f"➲ **Your Offline Duration**: `{formatted_elapsed_time}` 🥺"
        )
        return False  # Prevent further processing
    return True  # Allow processing if not AFK

# Command to set AFK status
@yuvaraj.on_message(filters.command("afk", prefixes=HANDLER) & filters.me)
async def set_afk(_, message):
    Busy_time = datetime.now()
    if len(message.command) < 2:
        # No reason provided
        await SET_AFK(Busy_time, None)
        await message.reply_text("➲ Successfully set you in AFK mode!")
    else:
        # Reason provided
        Reason_Of_Busy = " ".join(message.command[1:])
        await SET_AFK(Busy_time, Reason_Of_Busy)
        await message.reply_text(f"➲ Successfully set you in AFK mode!")

# Listener to detect when the user sends a message and remove AFK status
@yuvaraj.on_message(filters.me & filters.create(afk_remove))
async def remove_busy_mode(_, message):
    pass

# Module information
MOD_NAME = "Afk"
MOD_HELP = ".afk <reason (optional)> - To set you in AFK mode. If anyone DMs you, they will get alerted!"
