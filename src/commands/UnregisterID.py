import discord
from discord.ext import commands
from utils.dbManager import removeID

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

        resp: int = removeID(hiveid)

        if resp == 200:
            text = f"ID `{hiveid}` successfully removed"
        elif resp == 404:
            text = f"ID `{hiveid}` not found"
        elif resp == 500:
            text = "No registered IDs"
        else:
            text = "Unknown error, contact the developer"    

        await ctx.respond(text, ephemeral=True, delete_after=7)

def setup(bot):
    bot.add_cog(UnregisterID(bot))