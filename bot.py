import discord
import random
import datetime
import time
import linecache
from discord.ext import commands

TOKEN = 'NDU3NzA5MTExNjEwNTcyODEw.DgeZrw.DLKKmDtoFBYYVjVgMJ1diGexV5k'

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('beep boop bop')

@client.event
async def goodmorning(cxt):
    now = datetime.datetime.now()
    if now.hour == 8:
        await client.send_message(cxt, "Good morning!")

@client.command()
async def imaqtpie():
    await client.say('Doot diddly donger cuckerino... HAHA!')

@client.command()
async def joke():
    jokenum = random.randint(1,12)
    await client.say(linecache.getline('jokes.txt', jokenum))       #textfiles must be in utf-8 format
    time.sleep(1)
    await client.say('...')
    time.sleep(1)
    await client.say(linecache.getline('punchlines.txt', jokenum))

client.run(TOKEN)