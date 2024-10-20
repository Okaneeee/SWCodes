from discord.ext import commands
from utils.logger import Logger

LOGGER = Logger()

class onReadyEvent(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        LOGGER.log("Bot is up!", "INFO")
        LOGGER.log(f'Logged in as {self.bot.user}', "INFO")

def setup(bot):
    bot.add_cog(onReadyEvent(bot))