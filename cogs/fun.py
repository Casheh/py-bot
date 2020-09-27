import discord
import asyncio
from resources import eightball_responses, image_links
from PIL import Image, ImageDraw, ImageFont
import textwrap
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
        embed = discord.Embed(description=f'Outcome: {random.choice(eightball_responses.responses)}',
                              color=discord.Color.purple())
        # embed.set_author()
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

    # @commands.command()
    # async def liam(self, ctx):
    #     x = 0
    #     while x < 5:
    #         await ctx.send('Oi cunt <@214900730564182016>')
    #         x = x+1

    @commands.command()
    async def pingroulette(self, ctx):
        member = random.choice(ctx.guild.members).mention
        embed = discord.Embed(title='Chosing a user in 3...', color=discord.Color.purple())
        embed.set_footer(text='Pasta Man | Roulette', icon_url=self.client.user.avatar_url)
        msg = await ctx.send(embed=embed)

        await asyncio.sleep(1)
        embed.title = 'Chosing a user in 2...'
        await msg.edit(embed=embed)
        await asyncio.sleep(1)
        embed.title = 'Chosing a user in 1...'
        await msg.edit(embed=embed)
        await asyncio.sleep(1)
        await ctx.send(member + '\n' + member + '\n' + member
         +'\n' + member + '\n' + member + '\n' + member + '\n' + member)

    
    @commands.command()
    async def icreate(self, ctx, *, message):
    
        astr = f'''{message}'''
        para = textwrap.wrap(astr, width=35)

        MAX_W, MAX_H = 400, 200
        im = Image.new('RGB', (400, 200), (0, 0, 0, 0))
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype('arial.ttf', 18)

        current_h, pad = 10, 10
        for line in para:
            w, h = draw.textsize(line, font=font)
            draw.text(((MAX_W - w) / 2, current_h), line, font=font)
            current_h += h + pad

        im.save('img01.png')

        with open('img01.png', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)




def setup(client):
    client.add_cog(Fun(client))
