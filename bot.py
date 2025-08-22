import discord
from discord.ext import commands
import config
import os

#Configura o Bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=config.PREFIX, intents=intents)

#evento de inicialização
@bot.event
async def on_ready():
    print(f"🤖 {bot.user} está Online!")