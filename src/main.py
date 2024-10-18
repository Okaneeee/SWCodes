import os
import discord
from bot import SWCodes

class Main():
    @staticmethod
    def run():
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        try:
            token = open(os.path.join(__location__, "token"), "r").read().strip("\n")
        except FileNotFoundError:
            quit("Please create a token file and place your token in it!")
        if token is None:
            quit("Please create a token file and place your token in it!")
        else:
            intent = discord.Intents.all()
            intent.members = True
            intent.message_content = True

            bot = SWCodes(intent)
            bot.run(token)

if __name__ == '__main__':
    Main.run()
