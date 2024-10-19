import discord
from discord.ext import commands
from os import getenv

class Help(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot
        self.ownerID = int(getenv('OWNERID')) # type: ignore
        
    @commands.slash_command(
        name="help",
        description="Shows the available commands"
    )
    async def help(self, ctx):
        user = await self.bot.fetch_user(self.ownerID)

        helpEmbed : discord.Embed = discord.Embed(title="Test", description="Shows the available commands", colour=discord.Colour.from_rgb(46, 169, 103))

        helpEmbed.add_field(name="Show this menu", value="`/help`", inline = False)
        helpEmbed.add_field(name="Use a code on an account", value="`/usecode [hiveID] [code]`", inline = False)
        helpEmbed.add_field(name="Register your HiveID", value="`/registerID [hiveID]`", inline = False)
        helpEmbed.add_field(name="Unregister your HiveID", value="`/unregisterID [hiveID]`", inline = False)
        helpEmbed.add_field(name="Use a code on all registered IDs", value="`/trigger [code]` \n*Only available to the developer*", inline = False)

        helpEmbed.set_footer(
            text=f"By {user.name}",
            icon_url = user.avatar
        )

        await ctx.respond(embed=helpEmbed)

def setup(bot):
    bot.add_cog(Help(bot))