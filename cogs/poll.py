import discord
from discord.ext import commands
import asyncio

class Poll(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def poll(self, ctx):
        embed = discord.Embed(title='What should the question be?', color=discord.Color.purple())
        await ctx.send(embed=embed)

        try:
            msg = await self.client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=15)
            await msg.delete()
            await ctx.message.delete()
            embed.title = f':bar_chart: {msg.content}'
            await ctx.send(embed=embed)
        except asyncio.TimeoutError:
            embed.title = ':x: Timed out! Please answer within 15 seconds!'
            message = await ctx.send(embed=embed)
            await message.delete(delay=3)

    # @commands.command()
    # async def give(self, ctx):
    #     msg= await ctx.send('test')
    #     await msg.add_reaction(emoji=)






def setup(client):
    client.add_cog(Poll(client))