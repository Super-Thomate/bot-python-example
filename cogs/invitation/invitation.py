import discord
import botconfig
from discord.ext import commands

class Invitation(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name='invite')
  async def hello(self, ctx, member: discord.Member = None):
    """Send the url invitation link in a DM"""
    member = member or ctx.author
    try:
      await member.send (botconfig.config['invite_bot'])
    except:
      await ctx.message.channel.send ('Oups je ne peux pas envoyer de DM !')