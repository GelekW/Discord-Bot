import discord
import random
import datetime
import time
import linecache
from discord.ext import commands

TOKEN = ''

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('beep boop bop')

@client.command()
async def imaqtpie():
    await client.say('Doot diddly donger cuckerino... HAHA!')

@client.command(pass_context = True)
async def clear(ctx):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit = 100):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('Messages deleted. beep boop bop')

@client.command()
async def joke():
    jokenum = random.randint(1,12)
    await client.say(linecache.getline('jokes.txt', jokenum))       #textfiles must be in utf-8 format
    time.sleep(1)
    await client.say('...')
    time.sleep(1)
    await client.say(linecache.getline('punchlines.txt', jokenum))

@client.command(pass_context=True)
async def play(ctx, url):
    author = ctx.message.author
    voice_channel = author.voice_channel
    Bot = await client.join_voice_channel(voice_channel)

    player = await Bot.create_ytdl_player(url)
    player.start()

client.run(TOKEN)