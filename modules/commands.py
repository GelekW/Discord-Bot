import random
import datetime
import time
import linecache
from discord.ext import commands
import discord

class fun:

    @bot.command()
    async def imaqtpie():
        await bot.say('Doot diddly donger cuckerino... HAHA!')

    @bot.command(pass_context = True)
    async def clear(ctx):
        channel = ctx.message.channel
        messages = []
        async for message in bot.logs_from(channel, limit = 20):
            messages.append(message)
        await bot.delete_messages(messages)

        await bot.say('Messages deleted. beep boop bop')

    @bot.command()
    async def joke():
        jokenum = random.randint(1,12)
        await bot.say(linecache.getline('jokes.txt', jokenum))       #textfiles must be in utf-8 format
        time.sleep(1)
        await bot.say('...')
        time.sleep(1)
        await bot.say(linecache.getline('punchlines.txt', jokenum))

    @bot.command(pass_context=True)
    async def play(ctx, url):
        author = ctx.message.author
        voice_channel = author.voice_channel
        Bot = await bot.join_voice_channel(voice_channel)

        player = await Bot.create_ytdl_player(url)
        player.start()

def setup(bot):
    bot.add_cog(fun(bot))