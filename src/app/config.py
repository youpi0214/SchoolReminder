import os

import discord
from dotenv import load_dotenv

### Load environment variables ###
load_dotenv(verbose=True)
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

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


def getIntents():
    return intents
