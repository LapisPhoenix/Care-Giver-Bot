import os
import discord
from discord.ext import commands


class Support(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def support(self, ctx):
        embed = discord.Embed(
            title="Support",
            description="Subscribe to my [YouTube Channel](https://www.youtube.com/channel/UC0JbuZxOU1b0lC6N_Js7_sg)\nMy [Website](https://www.lapispheonix.com)",
            colour=0x00FF00,
        )

        embed.add_field(name="Invite Me", value=f"[Click Here]({os.getenv('INVITELINK')})")

        embed.set_footer(text="Spread Positivity!")

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Support(bot))