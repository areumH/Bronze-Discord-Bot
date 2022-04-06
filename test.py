import discord
from discord.ext import commands
from TkSave import Token

game = discord.Game("맨땅에 헤딩하며 개발")
bot = commands.Bot(command_prefix = "!", status = discord.Status.online, activity = game)

bot.run(Token)