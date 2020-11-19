# Nzc1MzU3NTYxNzkxNTc4MTMy.X6lKAA.t0aRqmqkWe6sm-dDppp9riFvWfo
import discord

class MyClient(discord.Client):
    async def on_ready(self):
        await self.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for messages that start with a dash (-)"))
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == client.user:
            return
        print('Message from {0.author}: {0.content}'.format(message))
        
        if message.content.startswith('-hello'):
            msg = 'Hello {0.author.mention}'.format(message)
            await message.channel.send(msg)

        if message.content.startswith('-blast'):
            msg = '{0.author.mention} WANTS TO PING @everyone'.format(message)
            await message.channel.send(msg)


client = MyClient()
client.run('Nzc1MzU3NTYxNzkxNTc4MTMy.X6lKAA.t0aRqmqkWe6sm-dDppp9riFvWfo')