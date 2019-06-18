import discord
import sys
from discord.ext import commands
import botconfig

def log(user, log_message):
  print ('[{0}] {1}: {2}'.format(date.today(), user, log_message))
def get_prefix(bot, message):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""
    prefixes = '!'
    return commands.when_mentioned_or(*prefixes)(bot, message)

# Define all of our cogs
initial_extensions = [   'cogs.greetings'
                       , 'cogs.invitation'
                     ]

bot = commands.Bot(command_prefix=get_prefix)

# Here we load our extensions(cogs) listed above in [initial_extensions].
if __name__ == '__main__':
  for extension in initial_extensions:
    bot.load_extension(extension)


@bot.event
async def on_ready():
  print('------')
  print('Logged in as')
  print(bot.user.name)
  print(bot.user.id)
  print('------')
  print('Discord.py version')
  print(discord.__version__)
  print('------')
  try:
    await bot.change_presence(activity=discord.Game(name="Bot test"))
  except TypeError as type_err:
    print ("Error TypeError : {}".format(type_err))
    sys.exit(0)
  except :
    print ("Error {}".format(sys.exc_info()[0]))
    sys.exit(0)

bot.run(botconfig.config['token'])