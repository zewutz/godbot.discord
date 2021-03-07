import discord
import os
from discord.ext import commands, tasks
from discord.ext.commands import CommandNotFound
from itertools import cycle
from web import web_server


client = commands.Bot(command_prefix='g!')
client.remove_command('help')

def bot_owner(ctx):
  return ctx.author.id == 266247738063060992

#On Ready
@client.event
async def on_ready():
    change_status.start()
    await client.change_presence(activity=discord.Game(name="god!help"))
    intents = discord.Intents
    intents.members = True
    print('We have logged in as {0.user}'.format(client))
    guilds = []
    for guild in client.guilds:
      guilds.append(guild)

    print(f'GodBot is connected to {len(guilds)} servers.')

    print("\n")

# Load/Unload Cogs

#Load
@client.command()
@commands.check(bot_owner)
async def load(ctx, extension):
  try:
    client.load_extension(f"cogs.{extension}")
  except:
    await ctx.send(f"Cannot load {extension} cog.")

@load.error
async def load_errors(ctx,error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("Please pass a cog Mr.Zewutz.")

#Unload
@client.command()
@commands.check(bot_owner)
async def unload(ctx, extension):
  try:
    client.unload_extension(f"cogs.{extension}")
  except:
    await ctx.send(f"Cannot unload {extension} cog.")

@unload.error
async def unload_errors(ctx,error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("Please pass a cog Mr.Zewutz.")

#Refresh 
@client.command()
@commands.check(bot_owner)
async def refresh(ctx, extension):
  try:
    client.load_extension(f"cogs.{extension}")
    client.unload_extension(f"cogs.{extension}")
  except:
    await ctx.send(f"Cannot refresh {extension}.")


@refresh.error
async def refresh_errors(ctx,error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("Please pass a cog Mr.Zewutz.")


for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')


#Command not found
@client.event
async def on_command_error(ctx, error):
  if isinstance(error, CommandNotFound):
      await ctx.send("Command not found.")

# JOIN 
@client.event
async def on_member_join(member):
  print(f'[NEW] {member} has joined.')

# LEAVE
@client.event
async def on_member_remove(member):
  print(f'[LEFT] {member} has left the server')


#Change status
bot_status = cycle(["g!help","Working on me.."])
@tasks.loop(seconds=10)
async def change_status():
  await client.change_presence(activity=discord.Game(next(bot_status)))


# @client.event()
# async def rainbowrole():
#   colours = cycle(["#ff0000",
#                     "#ffa500",
#                     "#ffff00",
#                     "#008000",
#                     "#0000ff",
#                     "#4b0082",
#                     "#4b0082"])

#   for role in guild.id(809125737041887308) :
#     if role.name == 'TANK':
#       await role.edit(colour=discord.Colour(next(colours)))

web_server()
client.run(os.getenv("TOKEN"))