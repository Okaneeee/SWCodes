import discord
from discord.ext import commands

class SlashCommand(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot
        
    @commands.slash_command(
        name="test",
        description="This is a simple slash command",
        guild_ids=[1266543874562588797]
    )
    async def test(self, ctx):
        user = await self.bot.fetch_user(430416407554031616)
        embedSC : discord.Embed = discord.Embed(title="Test", colour=discord.Colour.from_rgb(46, 169, 103))
        embedSC.set_footer(text="By okane.exe",
            icon_url = user.avatar) # type: ignore
        await ctx.respond(embed=embedSC)

def setup(bot):
    bot.add_cog(SlashCommand(bot))