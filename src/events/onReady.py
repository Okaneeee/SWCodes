from discord.ext import commands

class onReadyEvent(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("\n[INFO] Bot is up!")
        print(f'[INFO] Logged in as {self.bot.user}')

def setup(bot):
    bot.add_cog(onReadyEvent(bot))