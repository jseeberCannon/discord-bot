import random
import math
from discord.ext.commands import Bot

BOT_PREFIX = ("?")
TOKEN = 'Nzc1MzU3NTYxNzkxNTc4MTMy.X6lKAA.t0aRqmqkWe6sm-dDppp9riFvWfo'

client = Bot(command_prefix=BOT_PREFIX)

@client.command(name='8ball',
                description="Answers a yes/no question",
                brief="Answser your question",
                aliases=["eight_ball", "eightball", "8-ball"],
                pass_context=True)
async def eight_ball(message):
        possible_responses = [
            "Yes",
            "Possibly",
            "No"
        ]
        await message.channel.send(random.choice(possible_responses) + ", " + message.author.mention)

def square(message):
    squared_value = int(number) * int(number)
    await message.channel.send(str(number) + " squared is " + str(squared_value))

client.run(TOKEN)