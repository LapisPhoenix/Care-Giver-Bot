import os
import discord
import aiosqlite
from lib import logging
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

token = os.getenv("BOTTOKEN")
prefix = os.getenv("PREFIX")

bot = commands.Bot(
    command_prefix=prefix,
    intents=discord.Intents.all(),
    case_insensitive=True,
    description="Spread Positivity",
    help_command=None
)


@bot.event
async def on_ready():
    logger = logging.Logger()

    db = await aiosqlite.connect("database.db")
    await db.execute(
        "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, thankTokensGiven INTEGER, loveTokensGiven INTEGER, careTokensGiven INTEGER, thankTokensReceived INTEGER, loveTokensReceived INTEGER, careTokensReceived INTEGER)"
    )

    await db.commit()

    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            name = file[:-3]
            try:
                await bot.load_extension(f"cogs.{name}")
            except Exception as e:
                logger.log(f"Failed to load cogs.{name} with error: {e}", level="ERROR")
            print(f"Loaded cogs.{name}")

    print("Bot is ready")
    logger.log(f"Logged in as {bot.user.name}#{bot.user.discriminator}")
    print(f"ID: {bot.user.id}")
    print(f"Prefix: {prefix}")


bot.run(token)
