import discord
from discord.ext import commands
from utils.fetcher import multiFetch

class Trigger(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot
        
    @commands.slash_command(
        name="trigger",
        description="Use a code on all registered Hive IDs",
        options=[
            discord.Option(
                type=discord.SlashCommandOptionType.string,
                name="code",
                description="The code to use",
                required=True
            )
        ]
    )
    @commands.is_owner()
    async def trigger(self, ctx, code : str):
        resp, errors = multiFetch(code)

        if resp in [302, 306, 404, 500]:
            await ctx.respond(errors, ephemeral=True, delete_after=7)
        else:
            resultEmbed: discord.Embed = discord.Embed(
                title="Results",
                description=f"Used the code `{code}` on all registered IDs",
                colour=discord.Colour.from_rgb(57, 186, 128)
            )

            resultEmbed.add_field(name="Success", value=f"for {resp} accounts", inline=False)

            if errors:
                for error in errors:
                    title, val = error.split(" ", 1)
                    resultEmbed.add_field(name=title, value=val, inline=False)

            resultEmbed.set_footer(text="Contact the developer for more information")

            await ctx.respond(embed=resultEmbed, ephemeral=True, delete_after=7)

    # Handling errors
    @trigger.error
    async def trigger_error(self, ctx, error):
        await ctx.respond("You don't have the permission to do that.", ephemeral=True, delete_after=7)

def setup(bot):
    bot.add_cog(Trigger(bot))