import discord
import asyncio
import ahhMessages
import ahhSecret

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')


@client.event
async def on_message(message):
    if message.content.startswith('$dab'):
       await client.send_message(message.channel, ahhMessages.Test)

#Run locally
client.run(ahhSecret.Token)