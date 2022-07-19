import json
import discord
from discord.ext import commands
import os

with open('Setting.json', 'r', encoding = 'utf8') as file:
    file_data = json.load(file)

bot = commands.Bot(command_prefix="!")

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done.')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'UnLoaded {extension} done.')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'ReLoaded {extension} done.')

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        print(filename)
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(file_data['Token'])