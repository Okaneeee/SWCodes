import discord
from discord.ext import commands
import os

print("[INFO] Starting bot...")

class SWCodes(commands.Bot):
    def __init__(self, intents, prefix = "!"):
        commands.Bot.__init__(self, command_prefix=prefix, intents = intents)
        
        # Set activity
        self.activity = discord.Activity(type=discord.ActivityType.playing, name="Summoners War")

        # Events
        print("[INFO] Loading events...")
        for file in os.listdir("./src/events"):
            if file.endswith(".py"):
                self.load_extension("events." + file[:-3])
                print(file[:-3] + " event is UP !")

        print("[INFO] Events are loaded!")

        # Slash commands
        print("[INFO] Cooking slash commands...")
        for file in os.listdir("./src/commands"):
            if file.endswith(".py"):
                self.load_extension("commands." + file[:-3])
                print(file[:-3] + " command is ready!")

        print("[INFO] Slash commands are cooked!")