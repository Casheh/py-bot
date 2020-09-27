import bot_token
import os
import discord
from discord.ext import commands


client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print('Cybermod PRE_ALPHA V1.0.0')
    await client.change_presence(activity=discord.Game('FORNIT BATL ROYAEL'))

@client.command()
async def reloadall(ctx):
    for file in os.listdir('cogs'):
        if file.endswith('py'):
            client.unload_extension(f'cogs.{file[:-3]}')
            client.load_extension(f'cogs.{file[:-3]}')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title=':x: No permission!', colour=discord.Color.purple())
    elif isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(title=':x: Command not found!', colour=discord.Color.purple())
    else:
        embed = discord.Embed(title=':x: An error has occured.', color=discord.Color.purple())
    message = await ctx.send(embed=embed)
    await message.delete(delay=5)

for file in os.listdir('cogs'):
    if file.endswith('py'):
        client.load_extension(f'cogs.{file[:-3]}')


client.run(bot_token.token)
