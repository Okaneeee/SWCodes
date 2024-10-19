from os import getenv
import discord
from bot import SWCodes
from dotenv import load_dotenv
import sys

class Main():
    @staticmethod
    def run():
        load_dotenv()
        TOKEN = getenv('TOKEN')
        if TOKEN is None:
            sys.exit("Please create a token file and place your token in it!")
        else:
            intent = discord.Intents.all()
            intent.members = True
            intent.message_content = True

            bot = SWCodes(intent)
            bot.run(TOKEN)

if __name__ == '__main__':
    Main.run()
