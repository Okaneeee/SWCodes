import discord
from discord.ext import commands
from utils.fetcher import fetch

class UseCode(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot
        
    @commands.slash_command(
        name="usecode",
        description="Use a code on an account",
        options=[
            discord.Option(
                type=discord.SlashCommandOptionType.string,
                name="hiveid",
                description="The Hive ID of the account",
                required=True
            ),
            discord.Option(
                type=discord.SlashCommandOptionType.string,
                name="code",
                description="The code to use",
                required=True
            )
        ]
    )
    async def useCode(self, ctx, hiveid : str, code : str):
        text: str
        rCode, resp = fetch(hiveid, code)
        
        if rCode in [100, 304]:
            text = f"The account with the ID `{hiveid}` {resp}"
        elif rCode == 503:
            text = f"The hive ID `{hiveid}` is invalid."
        else:
            text = resp

        await ctx.respond(text, ephemeral=True, delete_after=7)

def setup(bot):
    bot.add_cog(UseCode(bot))