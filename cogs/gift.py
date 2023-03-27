import discord
import aiosqlite
from discord.ext import commands


class Gift(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def care(self, ctx, member: discord.Member):
        db = await aiosqlite.connect("database.db")

        giver = await db.execute("SELECT * FROM users WHERE id = ?", (ctx.author.id,))
        giver = await giver.fetchone()

        receiver = await db.execute("SELECT * FROM users WHERE id = ?", (member.id,))
        receiver = await receiver.fetchone()

        if giver is None:
            await db.execute(
                "INSERT INTO users (id, thankTokensGiven, loveTokensGiven, careTokensGiven, thankTokensReceived, loveTokensReceived, careTokensReceived) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (ctx.author.id, 0, 0, 0, 0, 0, 0),
            )
            await db.commit()
            giver = await db.execute(
                "SELECT * FROM users WHERE id = ?", (ctx.author.id,)
            )

            giver = await giver.fetchone()

        if receiver is None:
            await db.execute(
                "INSERT INTO users (id, thankTokensGiven, loveTokensGiven, careTokensGiven, thankTokensReceived, loveTokensReceived, careTokensReceived) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (member.id, 0, 0, 0, 0, 0, 0),
            )
            await db.commit()
            receiver = await db.execute(
                "SELECT * FROM users WHERE id = ?", (member.id,)
            )
            receiver = await receiver.fetchone()

        if giver[0] == receiver[0]:
            await ctx.send("You can't give tokens to yourself!")
            return

        await db.execute(
            "UPDATE users SET careTokensGiven = careTokensGiven + 1 WHERE id = ?",
            (ctx.author.id,),
        )

        await db.execute(
            "UPDATE users SET careTokensReceived = careTokensReceived + 1 WHERE id = ?",
            (member.id,),
        )

        await db.commit()

        embed = discord.Embed(title="Care Token", color=0x00FF00)

        embed.add_field(name="Giver", value=f"{ctx.author.mention}")
        embed.add_field(name="Receiver", value=f"{member.mention}")

        embed.add_field(
            name=f"Given",
            value=f"{ctx.author.mention} has now given **{giver[3] + 1}** care tokens!",
            inline=False
        )
        embed.add_field(
            name=f"Received",
            value=f"{member.mention} has now received **{receiver[6] + 1}** care tokens!",
            inline=False
        )

        embed.set_footer(text="Thank you for spreading positivity!")

        await ctx.send(embed=embed)

    ###############################################################################################################

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def love(self, ctx, member: discord.Member):
        db = await aiosqlite.connect("database.db")

        giver = await db.execute("SELECT * FROM users WHERE id = ?", (ctx.author.id,))
        giver = await giver.fetchone()

        receiver = await db.execute("SELECT * FROM users WHERE id = ?", (member.id,))
        receiver = await receiver.fetchone()

        if giver is None:
            await db.execute(
                "INSERT INTO users (id, thankTokensGiven, loveTokensGiven, careTokensGiven, thankTokensReceived, loveTokensReceived, careTokensReceived) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (ctx.author.id, 0, 0, 0, 0, 0, 0),
            )
            await db.commit()
            giver = await db.execute(
                "SELECT * FROM users WHERE id = ?", (ctx.author.id,)
            )

            giver = await giver.fetchone()

        if receiver is None:
            await db.execute(
                "INSERT INTO users (id, thankTokensGiven, loveTokensGiven, careTokensGiven, thankTokensReceived, loveTokensReceived, careTokensReceived) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (member.id, 0, 0, 0, 0, 0, 0),
            )
            await db.commit()
            receiver = await db.execute(
                "SELECT * FROM users WHERE id = ?", (member.id,)
            )

            receiver = await receiver.fetchone()

        if giver[0] == receiver[0]:
            await ctx.send("You can't give tokens to yourself!")
            return

        await db.execute(
            "UPDATE users SET loveTokensGiven = loveTokensGiven + 1 WHERE id = ?",
            (ctx.author.id,),
        )

        await db.execute(
            "UPDATE users SET loveTokensReceived = loveTokensReceived + 1 WHERE id = ?",
            (member.id,),
        )

        await db.commit()

        embed = discord.Embed(title="Love Token", color=0x00FF00)

        embed.add_field(name="Giver", value=f"{ctx.author.mention}")
        embed.add_field(name="Receiver", value=f"{member.mention}")

        embed.add_field(
            name=f"Given",
            value=f"{ctx.author.mention} has now given **{giver[2] + 1}** love tokens!",
            inline=False
        )
        embed.add_field(
            name=f"Received",
            value=f"{member.mention} has now received **{receiver[5] + 1}** love tokens!",
            inline=False
        )

        embed.set_footer(text="Thank you for spreading positivity!")

        await ctx.send(embed=embed)

    ###############################################################################################################

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def thank(self, ctx, member: discord.Member):
        db = await aiosqlite.connect("database.db")

        giver = await db.execute("SELECT * FROM users WHERE id = ?", (ctx.author.id,))
        giver = await giver.fetchone()

        receiver = await db.execute("SELECT * FROM users WHERE id = ?", (member.id,))
        receiver = await receiver.fetchone()

        if giver is None:
            await db.execute(
                "INSERT INTO users (id, thankTokensGiven, loveTokensGiven, careTokensGiven, thankTokensReceived, loveTokensReceived, careTokensReceived) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (ctx.author.id, 0, 0, 0, 0, 0, 0),
            )
            await db.commit()
            giver = await db.execute(
                "SELECT * FROM users WHERE id = ?", (ctx.author.id,)
            )

            giver = await giver.fetchone()

        if receiver is None:
            await db.execute(
                "INSERT INTO users (id, thankTokensGiven, loveTokensGiven, careTokensGiven, thankTokensReceived, loveTokensReceived, careTokensReceived) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (member.id, 0, 0, 0, 0, 0, 0),
            )
            await db.commit()
            receiver = await db.execute(
                "SELECT * FROM users WHERE id = ?", (member.id,)
            )
            receiver = await receiver.fetchone()

        if giver[0] == receiver[0]:
            await ctx.send("You can't give tokens to yourself!")
            return

        await db.execute(
            "UPDATE users SET thankTokensGiven = thankTokensGiven + 1 WHERE id = ?",
            (ctx.author.id,),
        )

        await db.execute(
            "UPDATE users SET thankTokensReceived = thankTokensReceived + 1 WHERE id = ?",
            (member.id,),
        )

        await db.commit()

        embed = discord.Embed(title="Thank Token", color=0x00FF00)

        embed.add_field(name="Giver", value=f"{ctx.author.mention}")
        embed.add_field(name="Receiver", value=f"{member.mention}")

        embed.add_field(
            name=f"Given",
            value=f"{ctx.author.mention} has now given **{giver[1] + 1}** thank tokens!",
            inline=False
        )
        embed.add_field(
            name=f"Received",
            value=f"{member.mention} has now received **{receiver[4] + 1}** thank tokens!",
            inline=False
        )

        embed.set_footer(text="Thank you for spreading positivity!")

        await ctx.send(embed=embed)

    ###############################################################################################################


async def setup(bot):
    await bot.add_cog(Gift(bot))
