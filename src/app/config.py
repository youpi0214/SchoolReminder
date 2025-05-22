import os

import discord
from dotenv import load_dotenv

### Load environment variables ###
load_dotenv(verbose=True)

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
if not DISCORD_TOKEN:
    raise ValueError("DISCORD_TOKEN is not set in the environment variables. Please set it and try again.")

BOT_NAME = os.getenv("BOT_NAME")
if not BOT_NAME:
    raise ValueError("BOT_NAME is not set in the environment variables. Please set it and try again.")

### Set up the intents ###
intents = discord.Intents.default()
# unwanted intents
intents.typing = False
intents.presences = False
intents.dm_typing = False
intents.dm_reactions = False
intents.dm_messages = False
intents.guild_typing = False
intents.guild_reactions = False

# wanted intents
intents.message_content = True
intents.guilds = True
intents.messages = True
intents.guild_messages = True
intents.members = True


def getIntents():
    return intents
