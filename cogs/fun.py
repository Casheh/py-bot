import discord
import asyncio
from resources import image_links, eightball_responses
import random
from discord.ext import commands

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client



    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot and 'hello' in message.content.lower():
            await message.channel.send(f'Hello, {message.author.mention}')

    @commands.command()
    async def lol(self, ctx):
        embed = discord.Embed(title='LOL', color=discord.Color.purple())
        rand = random.choice(image_links.images)
        embed.set_image(url=rand)
        embed.set_footer(text='Pasta Man | Fun', icon_url=self.client.user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def pizza(self, ctx):
        embed = discord.Embed(title="HERE'S YOU'RE DAMN PIZZA", color=discord.Color.purple())
        rand = random.choice(image_links.pizza_pics)
        embed.set_image(url=rand)
        embed.set_footer(text='Pasta Man | Pizza of The Day', icon_url=self.client.user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def pasta(self, ctx):
        embed = discord.Embed(title="HERE'S YOU'RE DAMN PASTA", color=discord.Color.purple())
        rand = random.choice(image_links.pasta_pics)
        embed.set_image(url=rand)
        embed.set_footer(text='Pasta Man | Pasta of The Day', icon_url=self.client.user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases=['coin', 'coinflip'])
    async def flip(self, ctx):

        embed = discord.Embed(title=f"the coin landed on {random.choice(['heads', 'tails'])}!", color=discord.Color.purple())
        message = await ctx.send('Flipping...')
        await asyncio.sleep(.5)
        embed.set_footer(text='Pasta Man | Coin Flip', icon_url=self.client.user.avatar_url)
        await message.edit(embed=embed)



    @commands.command(aliases=['8ball', 'magicball'])
    async def _8ball(self, ctx, *, question):
        embed = discord.Embed(title=f':8ball: {question}',
                              description=f'Outcome: {random.choice(eightball_responses.responses)}',
                              color=discord.Color.purple())
        await ctx.send(embed=embed)


    @commands.command()
    async def fortnite(self, ctx):
        if not ctx.author.bot:
            await ctx.author.send('https://www.youtube.com/watch?v=CI4mNS7oax4&t=2s')


    @commands.command()
    async def spam(self, ctx):
        x=0
        while x < 5:
            await ctx.author.send('https://www.youtube.com/watch?v=CI4mNS7oax4&t=2s')
            x = x+1



def setup(client):
    client.add_cog(Fun(client))