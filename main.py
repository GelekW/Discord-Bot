import discord
from discord.ext import commands
import modules
import configparser

bot = commands.Bot(command_prefix = '!')

extensions = ['commands', 'events']

@bot.event
async def on_ready():
    print('beep boop bop')


@bot.command()
async def load(extension_name : str):
    """Loads an extension."""
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await bot.say("{} loaded.".format(extension_name))

@bot.command()
async def unload(extension_name : str):
    """Unloads an extension."""
    bot.unload_extension(extension_name)
    await bot.say("{} unloaded.".format(extension_name))

if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as error:
            print('{} cannot be loaded [{}]'.format(extension, error))

config = configparser.ConfigParser()
config.read('config.ini')

bot.run(config.get(section='section_a', option='TOKEN'),
bot=True, reconnect=True)