from os import getenv
import discord
from bot import SWCodes
from dotenv import load_dotenv
import sys
from utils.logger import Logger

LOGGER = Logger()

class Main():
    @staticmethod
    def run():
        load_dotenv()
        TOKEN = getenv('TOKEN')
        if TOKEN is None:
            LOGGER.makeLog("Undefined token", "CRITICAL")
            sys.exit("Please provide a token in the .env file.")
        else:
            intent = discord.Intents.default()

            bot = SWCodes(intent)
            bot.run(TOKEN)

if __name__ == '__main__':
    Main.run()
