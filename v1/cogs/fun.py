import discord
import random
import datetime
from discord import Embed
from discord.ext import commands

class Fun(commands.Cog):
  def __init__(self,client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print("[Cog log] Fun package has loaded.")


    # RANDOM NUMBER
  @commands.command()
  async def dice(self,ctx):
      embed = Embed(
          colour=discord.Color.blue(),
          timestamp=datetime.datetime.now()
          
          ).add_field(
          name='Your numbers:',
          value=f"**{random.randint(1,6)} :game_die: {random.randint(1,6)}** ",
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


  @commands.command()
  async def askgod(self,ctx,* , question):
    responses = ["It is certain.",
                  "It is decidedly so.",
                  "Without a doubt.",
                  "Yes - definitely.",
                  "You may rely on it.",
                  "As I see it, yes.",
                  "Most likely.",
                  "Outlook good.",
                  "Yes.",
                  "Signs point to yes.",
                  "Reply hazy, try again.",
                  "Ask again later.",
                  "Better not tell you now.",
                  "Cannot predict now.",
                  "Concentrate and ask again.",
                  "Don't count on it.",
                  "My reply is no.",
                  "My sources say no.",
                  "Outlook not so good.",
                  "Very doubtful."]
    embed = Embed(
        colour=discord.Color.blue(),
        timestamp=datetime.datetime.now()
        
        ).add_field(
        name='Question:',
        value=f" ●  {question}?",
        inline=False

        ).add_field(
        name='Answer:',
        value=f" ●  {random.choice(responses)}",
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

  @askgod.error
  async def askgod_errors(ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send("No question passed. Try again.")



def setup(client):
  client.add_cog(Fun(client))