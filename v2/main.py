#!/usr/bin/python3
import discord
import os
from discord.ext import commands, tasks
from discord.ext.commands import CommandNotFound
from itertools import cycle

client = commands.Bot(command_prefix='>')
client.remove_command('help')

#! @zewutz id
def bot_owner(ctx):
  return ctx.author.id == 266247738063060992


@client.event
async def on_ready():
    """[when bot is running]
    - start changing status
    - enable intents
    - display servers 
    """
    #* Change status
    change_status.start()
    await client.change_presence(activity=discord.Game(name="god!help"))
    #* Intents
    intents = discord.Intents
    intents.members = True
    #* Log info
    print('We have logged in as {0.user}'.format(client))
    guilds = []
    for guild in client.guilds:
      guilds.append(guild)

    print(f'Bot is connected to {len(guilds)} servers.')

    print("\n")


#Load
@client.command()
@commands.check(bot_owner)
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"Loaded.")

#Unload
@client.command()
@commands.check(bot_owner)
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    await ctx.send(f"Unloaded.")

#Update
@client.command()
@commands.check(bot_owner)
async def update(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    client.unload_extension(f"cogs.{extension}")
    await ctx.send(f"Updated.")


for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')


#Change status
bot_stats = [">help","ig:@zewutz",">help","ig:@busa_fabian"]
bot_status = cycle(bot_stats)
@tasks.loop(seconds=10)
async def change_status():
  await client.change_presence(activity=discord.Game(next(bot_status)))

# Run bot
TOKEN = os.getenv('TOKEN')
client.run(TOKEN)