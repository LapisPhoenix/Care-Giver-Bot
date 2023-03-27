import discord
from discord.ext import commands


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("That command doesn't exist.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You are missing a required argument.")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("You are missing permissions to run this command.")
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send("I am missing permissions to run this command.")
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"This command is on cooldown. Try again in {round(error.retry_after)} seconds.")
        elif isinstance(error, commands.CommandInvokeError):
            await ctx.send("An error occurred while running this command.")
        elif isinstance(error, commands.DisabledCommand):
            await ctx.send("This command is disabled.")
        else:
            await ctx.send("An unknown error occurred.")
    
async def setup(bot):
    await bot.add_cog(Events(bot))