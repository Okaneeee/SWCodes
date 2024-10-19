import discord
from discord.ext import commands
from utils.dbManager import addID

class disclaimerView(discord.ui.View):
    def __init__(self, bot : commands.Bot, hiveid: str) -> None:
        super().__init__()
        self.bot = bot
        self.hiveid = hiveid

    @discord.ui.button(label="I acknowledge and accept.", style=discord.ButtonStyle.danger)
    async def agree(self, button: discord.ui.Button, interaction: discord.Interaction):
        
        rCode = addID(self.hiveid, interaction.user.id) # type: ignore
        if rCode == 200:

            answerEmbed: discord.Embed = discord.Embed(
                title="Your Hive ID is now registered!",
                description="It will be used to redeem codes on your account when the `trigger` command is used.",
                colour=discord.Colour.from_rgb(106, 34, 73)
            )

            answerEmbed.set_footer(
                text = f"{self.bot.user.name} | Thank you for your trust and support!", # type: ignore
                icon_url = self.bot.user.avatar # type: ignore
            )

        else:
            answerEmbed: discord.Embed = discord.Embed(
                title="Your Hive ID is already registered!",
                description="You can unregister it with the `/unregisterID` command.",
                colour=discord.Colour.from_rgb(253, 208, 23)
            )

            answerEmbed.set_footer(
                text = f"{self.bot.user.name} | Thank you for your trust and support!", # type: ignore
                icon_url = self.bot.user.avatar # type: ignore
            )

        await interaction.response.edit_message(embed=answerEmbed, delete_after=5, view=None)
        self.stop()

    @discord.ui.button(label="No, take me back!", style=discord.ButtonStyle.primary)
    async def disagree(self, button: discord.ui.Button, interaction: discord.Interaction):
        answerEmbed: discord.Embed = discord.Embed(
            title="Alright,",
            description="Your Hive ID won't be added.",
            colour=discord.Colour.from_rgb(52, 55, 126)
        )

        answerEmbed.set_footer(
            # use bot's avatar and name
            text = f"{self.bot.user.name} | Thank you for your trust and support!", # type: ignore
            icon_url = self.bot.user.avatar # type: ignore
        )

        await interaction.response.edit_message(embed=answerEmbed, delete_after=5, view=None)
        self.stop()

class RegisterID(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot
        
    @commands.slash_command(
        name="registerid",
        description="Register a Hive ID on the bot's database",
        options=[
            discord.Option(
                type=discord.SlashCommandOptionType.string,
                name="hiveid",
                description="The Hive ID of the account",
                required=True
            )
        ],
        guild_ids=[1266543874562588797]
    )
    async def registerID(self, ctx, hiveid : str):
        disclaimerEmbed: discord.Embed = discord.Embed(
            title="⚠️ Disclaimer ⚠️",
            description="By clicking on the button below, you agree to share your Hive ID with the bot. \n\
            This information will be stored in a private database and will only be used to redeem codes on your account. \n\
            Only the bot owner has access to this information and it will not be shared with anyone nor used for any other purpose.",
            colour=discord.Colour.from_rgb(255, 15, 15)
        )

        disclaimerEmbed.set_footer(
            text="Invoked by " + ctx.author.name,
            icon_url=ctx.author.avatar
        )

        await ctx.respond(embed=disclaimerEmbed, view=disclaimerView(self.bot, hiveid), ephemeral=True)

def setup(bot):
    bot.add_cog(RegisterID(bot))