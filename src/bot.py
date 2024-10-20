import discord
from discord.ext import commands
import os, sys
from utils.logger import Logger

LOGGER = Logger()
LOGGER.log("Starting bot...", "INFO")

class SWCodes(commands.Bot):
    def __init__(self, intents):
        ownerid = os.getenv("OWNERID")

        if ownerid is None:
            LOGGER.log("Undefined owner ID", "CRITICAL")
            sys.exit("Please provide an owner ID in the .env file.")

        commands.Bot.__init__(self, intents = intents, owner_id = int(ownerid))
        
        # Set activity
        self.activity = discord.Activity(type=discord.ActivityType.playing, name="Summoners War")

        # Events
        LOGGER.log("Loading events...", "INFO")
        for file in os.listdir("./src/events"):
            if file.endswith(".py"):
                self.load_extension("events." + file[:-3])
                print(file[:-3] + " event is UP !")

        LOGGER.log("Events are loaded", "INFO")

        # Slash commands
        LOGGER.log("Loading slash commands...", "INFO")
        for file in os.listdir("./src/commands"):
            if file.endswith(".py"):
                self.load_extension("commands." + file[:-3])
                print(file[:-3] + " command is ready!")

        LOGGER.log("Slash commands are loaded", "INFO")