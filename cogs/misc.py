import discord
from discord.ext import commands
import asyncio

import datetime

def chop_microseconds(delta):
    return delta-datetime.timedelta(microseconds=delta.microseconds)

def is_not_bot(member):
    if member.bot:
        return False
    else:
        return True


class Misc(commands.Cog):


    def __init__(self, client):
        self.client = client


    @commands.command(aliases=['quit'])
    async def close(self, ctx):
        if ctx.author.id == 365889701174837259:
            await self.client.close()
            print('Bot has been logged off')


    @commands.command()
    async def pfp(self, ctx, member: discord.Member=None):
        if member is None:
            img = ctx.author.avatar_url
            embed = discord.Embed(title=f'Pfp of {ctx.author}', color=discord.Color.purple())
        else:
            embed = discord.Embed(title=f'Pfp of {member}', color=discord.Color.purple())
            img = member.avatar_url
        embed.set_image(url=img)
        embed.set_footer(text='Pasta Man | Profile Picture', icon_url=self.client.user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def userinfo(self, ctx, *, member : discord.Member=None):
        if member is None:
            member = ctx.author

        embed = discord.Embed(title='User info: ', color=discord.Color.purple())
        embed.set_author(name=f'{member}', icon_url=member.avatar_url)
        embed.add_field(name='Creation date: ', value=f'{member.created_at.ctime()}', inline=True)
        embed.add_field(name='Join date: ', value=f'{member.joined_at.ctime()}', inline=True)
        embed.add_field(name='Server nick: ', value=f'{member.display_name}', inline=False)
        embed.add_field(name='Current status: ', value=f"{member.status}", inline=False)
        embed.add_field(name='Current activity: ', value=f"{member.activity}", inline=False)
        embed.add_field(name='Highest role: ', value=f'{member.top_role}', inline=False)
        embed.set_thumbnail(url=member.avatar_url)


        await ctx.send(embed=embed)


    @commands.command()
    async def serverinfo(self, ctx):

        embed = discord.Embed(title='Server info: ', color=discord.Color.purple())
        embed.set_author(name=f'{ctx.guild.name}', icon_url=ctx.guild.icon_url)
        embed.add_field(name='Voice channels: ', value=f'{len(ctx.guild.voice_channels)}', inline=True)
        embed.add_field(name='Text channels: ', value=f'{len(ctx.guild.text_channels)}', inline=True)
        embed.add_field(name='Creation date: ', value=f'{ctx.guild.created_at.ctime()}', inline=False)
        embed.add_field(name='Member count: ', value=f'{len(ctx.guild.members)}', inline=False)
        embed.add_field(name='Role count: ', value=f'{len(ctx.guild.roles)}', inline=False)
        embed.add_field(name='Server region: ', value=f'{ctx.guild.region}', inline=False)
        embed.add_field(name='Owner: ', value=f'{ctx.guild.owner.mention}', inline=False)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_footer(text='Pasta Man | Server Info', icon_url=self.client.user.avatar_url)

        await ctx.send(embed=embed)


    @commands.command()
    async def spotify(self, ctx, *, member: discord.Member=None):
        member = member or ctx.author

        embed = discord.Embed(title=f'{member} is listening to: ', color=discord.Color.green())
        embed.set_author(name='Spotify', icon_url='https://www.freepnglogos.com/uploads/spotify-logo-png/file-spotify-logo-png-4.png')
        embed.set_footer(text='Pasta Man | Spotify', icon_url=self.client.user.avatar_url)


        bool = False
        for activity in member.activities:
            if isinstance(activity, discord.Spotify):
                bool = True
                embed.add_field(name='Song title: ', value=f'{activity.title}', inline=True)
                embed.add_field(name='Artist: ', value=f'{activity.artist}', inline=True)
                embed.add_field(name='Album: ', value=f'{activity.album}', inline=True)
                embed.add_field(name='Length: ', value=f'{chop_microseconds(activity.duration)}', inline=False)
                embed.set_thumbnail(url=activity.album_cover_url)

        if not bool:
            embed2 = discord.Embed(title=':x: User not listening to Spotify!', color=discord.Color.red())
            await ctx.send(embed=embed2)
        else:
            await ctx.send(embed=embed)


    @commands.command(aliases=['interest', 'interestcheck'])
    async def ic(self, ctx, *, val):

        await ctx.message.delete()
        embed = discord.Embed(title=f'{val}', color=discord.Color.purple())
        msg = await ctx.send(embed=embed)
        try:
            await msg.add_reaction('☑')
            await self.client.wait_for('raw_reaction_add', check=is_not_bot(member=member), timeout=5)
        except asyncio.TimeoutError:
            embed = discord.Embed(title='Giveaway has ended!', colour=discord.Color.purple())
            await ctx.send(embed=embed)



def setup(client):
    client.add_cog(Misc(client))