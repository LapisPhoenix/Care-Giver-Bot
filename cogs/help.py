import os
import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        embed = discord.Embed(
            title="Help",
            description=f"Do `{os.getenv('PREFIX')}help <command>` for more info on a command.",
            colour=0x00FF00,
        )

        embed.add_field(
            name="Gift",
            value="`thank`, `love`, `care`",
        )

        embed.add_field(
            name="Utility",
            value="`help`, `ping`, `support`"
        )

        embed.set_footer(text="Spread Positivity!")

        await ctx.send(embed=embed)
    
    @help.command()
    async def thank(self, ctx):
        embed = discord.Embed(
            title="Thank",
            description="Thank someone for doing something nice for you!",
            colour=0x00FF00,
        )

        embed.add_field(
            name="Usage",
            value=f"`{os.getenv('PREFIX')}thank <member>`",
        )

        embed.set_footer(text="Spread Positivity!")

        await ctx.send(embed=embed)
    
    @help.command()
    async def love(self, ctx):
        embed = discord.Embed(
            title="Love",
            description="Spread some love for  someone for being a great person!",
            colour=0x00FF00,
        )

        embed.add_field(
            name="Usage",
            value=f"`{os.getenv('PREFIX')}love <member>`",
        )

        embed.set_footer(text="Spread Positivity!")

        await ctx.send(embed=embed)
    
    @help.command()
    async def care(self, ctx):
        embed = discord.Embed(
            title="Care",
            description="Care for someone for being a great person!",
            colour=0x00FF00,
        )

        embed.add_field(
            name="Usage",
            value=f"`{os.getenv('PREFIX')}care <member>`",
        )

        embed.set_footer(text="Spread Positivity!")

        await ctx.send(embed=embed)
    
    @help.group(invoke_without_command=True)
    async def help_group(self, ctx):
        embed = discord.Embed(
            title="Help",
            description="Get help with the bot!",
            colour=0x00FF00,
        )

        embed.add_field(
            name="Usage",
            value=f"`{os.getenv('PREFIX')}help`",
        )

        embed.set_footer(text="Spread Positivity!")

        await ctx.send(embed=embed)
    
async def setup(bot):
    await bot.add_cog(Help(bot))
