import discord
from discord.ext import commands


class MutedUser(commands.Converter):
    async def convert(self, ctx, argument):
        argument = await commands.MemberConverter().convert(ctx, argument)
        muted = discord.utils.get(ctx.guild.roles, name="Muted")
        if muted in argument.roles:
            return argument
        else:
            embed = discord.Embed(title="The user wasn't muted", color=discord.Color.purple())
            message = await ctx.send(embed=embed)
            await message.delete(delay=3)



async def mute(ctx, user, reason=None):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not role:
        try:
            muted = await ctx.guild.create_role(name="Muted", reason="Used for muting")
            for channel in ctx.guild.channels:
                await channel.set_permissions(muted,
                                              send_messages=False, read_message_history=False, read_messages=False)
        except discord.Forbidden:
            embed = discord.Embed(title=':x: Bot does not have permission to create roles!', colour=discord.Color.purple())
            message = await ctx.send(embed=embed)
            return await message.delete(delay=3)
        await user.add_roles(muted)
    else:
        await user.add_roles(role)

class Moderation(commands.Cog):



    def __init__(self, client):
        self.client = client


    @commands.command(aliases=['purge, clean'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=5):

        if 0 < amount <= 200:
            await ctx.channel.purge(limit=amount + 1)
            if amount == 1:
                embed = discord.Embed(title=f'{amount} message cleared!', colour=discord.colour.Color.purple())
            else:
                embed = discord.Embed(title=f'{amount} messages cleared!', colour=discord.colour.Color.purple())
        else:
            embed = discord.Embed(title=':x: You may not clear less than 1 message or more than 200!',
                                  colour=discord.Color.purple())
        message = await ctx.send(embed=embed)
        await message.delete(delay=3)


    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member : discord.Member, *, reason=None):
        await mute(ctx, member, reason=reason)
        if reason is not None:
            embed = discord.Embed(title=f'{member} has been muted for {reason}!', color=discord.Color.purple())
        else:
            embed = discord.Embed(title=f'{member} has been muted!', color=discord.Color.purple())
        message = await ctx.send(embed=embed)
        await message.delete(delay=3)


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        if reason is not None:
            await member.kick(reason=reason)
            embed = discord.Embed(title=f':white_check_mark: {member} has been kicked for {reason}!', color=discord.Color.purple())
        else:
            await member.kick()
            embed = discord.Embed(title=f':white_check_mark: {member} has been kicked!', color=discord.Color.purple())
        await ctx.send(embed=embed)


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        if reason is not None:
            await member.ban(reason=reason)
            embed = discord.Embed(title=f':white_check_mark: {member} has been banned for {reason}!',
                                  color=discord.Color.purple())
        else:
            await member.ban()
            embed = discord.Embed(title=f':white_check_mark: {member} has been banned!', color=discord.Color.purple())
        await ctx.send(embed=embed)


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discrim = member.split('#')

        for ban in banned_users:
            user = ban.user

            if (user.name, user.discriminator) == (member_name, member_discrim):
                await ctx.guild.unban(user)
                embed = discord.Embed(title=f':white_check_mark: {member} has been unbanned!', color=discord.Color.purple())
                await ctx.send(embed=embed)



    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, member : MutedUser):
        await member.remove_roles(discord.utils.get(ctx.guild.roles, name="Muted"))
        embed = discord.Embed(title=f'{member} has been unmuted!', colour=discord.colour.Color.purple())
        message = await ctx.send(embed=embed)
        await message.delete(delay=3)



def setup(client):
    client.add_cog(Moderation(client))