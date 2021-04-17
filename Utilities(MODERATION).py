import asyncio
import discord  # 40% yes 40% no 20% random
import random
import youtube_dl
import os
import ffmpeg

from discord.ext import commands
from discord.ext import commands
from discord.utils import get

bot = commands.Bot(command_prefix="c.")
randomthing = 0
players = {}


@bot.event
async def on_ready():
    print("connected and ready to use")



@bot.command(pass_context=True)
async def cmds(ctx):
    await ctx.send('c. is the prefix\n\nrename - c.rename <user> <new name>\nban - c.ban <user> <reason>\nkick - c.kick <user> <reason>\nunban - c.unban <user> <reason>')

@bot.command()
async def rename(ctx, user: discord.Member, *, newName=""):
    if ctx.message.author.guild_permissions.administrator:
        renameduser = user.nick
        await user.edit(nick=newName)
        await ctx.send(ctx.message.author.mention + " changed " + str(user.name) + "'s name to " + newName)
        print("command rename | " + str (renameduser.toString()) + " | " + newName)


@bot.command()
async def ban(ctx, user: discord.Member, *, reason=""):
    if ctx.message.author.guild_permissions.administrator:
        channel = await user.create_dm()
        await channel.send(reason)
        await user.ban(reason='barry benson hates u also...' + reason)
        await ctx.send(ctx.message.author.mention + " banned " + str(
            user.name) + "because barry bensen is always watching and " + reason)
        print("command ban | " + 'user' + " | " + reason)


@bot.command()
async def kick(ctx, user: discord.Member, *, reason=""):
    if ctx.message.author.guild_permissions.administrator:
        channel = await user.create_dm()
        await channel.send(reason)
        await user.ban(reason='barry benson hates u also...' + reason)
        await ctx.send(ctx.message.author.mention + " banned " + str(
            user.name) + "because barry bensen is always watching and " + reason)
        await user.unban(reason='barry likes you again :)')
        print("command kick | " + 'user' + " | " + reason)


@bot.command()
async def unban(ctx, user: discord.Member, *, reason=""):
    if ctx.message.author.guild_permissions.administrator:
        channel = await user.create_dm()
        await channel.send(reason)
        await user.unban(reason='barry likes you again :)')
        print("command unban | " + 'user' + " | " + reason)



@bot.event
async def on_command_error(ctx, error):
    print(f"An error occured: {str(error)}")


bot.run("ODI4MDc2MjY4OTA1OTU1Mzgx.YGkUHw.kNVnm-v3mVn3ldSkRynpkADeLns")