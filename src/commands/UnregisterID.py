import discord
from discord.ext import commands
from utils.dbManager import removeID
from utils.logger import Logger

LOGGER = Logger()

class UnregisterID(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot
        
    @commands.slash_command(
        name="unregisterid",
        description="Unregister a Hive ID on the bot's database",
        options=[
            discord.Option(
                type=discord.SlashCommandOptionType.string,
                name="hiveid",
                description="The Hive ID of the account",
                required=True
            )
        ]
    )
    async def unregisterID(self, ctx, hiveid : str):
        text: str = ""
        logText: str = f"UnregisterID command invoked by {ctx.author.name}:"

        resp: int = removeID(hiveid)

        if resp == 200:
            text = f"ID `{hiveid}` successfully removed"
            LOGGER.log(f"{logText} Hive ID successfully removed", "INFO")
        elif resp == 404:
            text = f"ID `{hiveid}` not found"
            LOGGER.log(f"{logText} Hive ID not found", "INFO")
        elif resp == 500:
            text = "No registered IDs"
            LOGGER.log(f"{logText} {text}", "INFO")
        else:
            text = "Unknown error, contact the developer"   
            LOGGER.log(f"{logText} {text}", "ERROR") 

        await ctx.respond(text, ephemeral=True, delete_after=7)

def setup(bot):
    bot.add_cog(UnregisterID(bot))