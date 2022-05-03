import discord
from discord.ext import commands

client = commands.Bot(command_prefix='$')


@client.event
async def on_ready():
    print('BOT connected')


@client.command(pass_context=True)
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount)


token = open('token.txt', 'r').readline()

client.run(token)