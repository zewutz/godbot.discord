import discord
import datetime
from discord import Embed
from discord.ext import commands

class _Help(commands.Cog): 
  def __init__(self,client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print("[Cog log] Help package has loaded.")

  @commands.command(aliases=["godhelpme","helpme","commands"])
  async def help(self,ctx):
      embed = Embed(
          title='GodBot Commands',
          description='My prefix: g!',
          colour=discord.Color.blue(),
          timestamp=datetime.datetime.now()
          
          ).add_field(
          name=':partying_face: Fun Commands',
          value=" `dice` `askgod`   ",
          inline=False

          ).add_field(
          name=':tools: Moderator commands',
          value=" `clear` `kick` `ban` `ping` `createrole` `setrole` ",
          inline=False

          ).set_footer(
          text=f'{str(ctx.author)[:-5]}',
          icon_url='https://cdn.discordapp.com/avatars/694446165197979670/eb946325b85f913abdec645d0c14b98a.webp?size=1024'

          ).set_image(
          url='https://cdn.discordapp.com/avatars/694446165197979670/eb946325b85f913abdec645d0c14b98a.webp?size=1024'

          ).set_thumbnail(
          url='https://cdn.discordapp.com/avatars/694446165197979670/eb946325b85f913abdec645d0c14b98a.webp?size=1024'
          )

      await ctx.send(embed=embed)



def setup(client):
  client.add_cog(_Help(client))