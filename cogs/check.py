import discord
import aiosqlite
from discord.ext import commands


class Check(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def check(
        self, ctx, member: discord.Member = commands.context.Context.author
    ):
        db = await aiosqlite.connect("database.db")

        embed = discord.Embed(
            title="Token Check",
            description=f"{ctx.author.mention} is checking {member.mention}'s tokens."
            if ctx.author.id != member.id
            else f"{ctx.author.mention} is checking their tokens.",
            color=0x00FF00,
        )

        stats = await db.execute("SELECT * FROM users WHERE id = ?", (member.id,))
        stats = await stats.fetchone()

        if stats is None:
            await db.execute(
                "INSERT INTO users (id, thankTokensGiven, loveTokensGiven, careTokensGiven, thankTokensReceived, loveTokensReceived, careTokensReceived) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (member.id, 0, 0, 0, 0, 0, 0),
            )
            await db.commit()
            stats = await db.execute(
                "SELECT * FROM users WHERE id = ?", (member.id,)
            )

            stats = await stats.fetchone()

        thankGiven = stats[1]
        loveGiven = stats[2]
        careGiven = stats[3]
        thankReceived = stats[4]
        loveReceived = stats[5]
        careReceived = stats[6]

        embed.add_field(
            name="Thank Tokens Given",
            value=f"{member.mention} has given **{thankGiven}** thank tokens.",
        )
        embed.add_field(
            name="Love Tokens Given",
            value=f"{member.mention} has given **{loveGiven}** love tokens.",
        )
        embed.add_field(
            name="Care Tokens Given",
            value=f"{member.mention} has given **{careGiven}** care tokens.",
        )
        embed.add_field(
            name="Thank Tokens Received",
            value=f"{member.mention} has received **{thankReceived}** thank tokens.",
        )
        embed.add_field(
            name="Love Tokens Received",
            value=f"{member.mention} has received **{loveReceived}** love tokens.",
        )
        embed.add_field(
            name="Care Tokens Received",
            value=f"{member.mention} has received **{careReceived}** care tokens.",
        )

        embed.set_footer(text="Thank you for spreading positivity!")

        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Check(bot))
