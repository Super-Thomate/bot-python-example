import discord
import botconfig
from discord.ext import commands

class Invitation(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name='invite')
  async def hello(self, ctx):
    """Send the url invitation link"""
    await ctx.message.channel.send (botconfig.config['invite_bot'])