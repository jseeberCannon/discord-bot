import random
from discord.ext.commands import Bot
from discord.ext import tasks
from itertools import cycle
import os
import discord
import json

with open('config.json') as f:
    config = json.load(f)
prefix = config['prefix']
token = config['token']

#BOT_PREFIX = ("?")
#TOKEN = ''

client = Bot(command_prefix=prefix)
status = cycle(['Status funny', 'Status unfunny'])

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.event
async def on_ready():
    print('Bot is ready')
    change_status.start()
    await client.change_presence(status=discord.Status.dnd)

@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)} ms')

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    
    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
            return

@client.command(name='8ball',
                description="Answers a yes/no question",
                brief="Answser your question",
                aliases=["eight_ball", "eightball", "8-ball"],
                pass_context=True)
async def eight_ball(ctx, *, question):
        responses = [
            "Yes",
            "Possibly",
            "No"
        ]
        await ctx.send(f'Question: {question}\nAnwser: {random.choice(responses)}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)