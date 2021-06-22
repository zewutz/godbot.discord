import discord
import os
import random
from discord.ext import commands

class AdminCommands(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print("[Cog log] Admin package has loaded.")
    
  #Clear
  @commands.command(name="clear")
  @commands.has_permissions(manage_messages=True)
  async def clear(self,ctx, amount=2):
    try:
      await ctx.channel.purge(limit=amount)
    except:
      await ctx.send('You are missing Manage Messages permission(s) to run this command.')


  #Kick
  @commands.command(name="kick")
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member : discord.Member, * ,reason = None):
    try:
      await member.kick(reason=reason)
      await ctx.send(f"{member} has been kicked by {ctx.author}.")
    except discord.ext.commands.errors.MissingPermissions:
      await ctx.send("You are missing Kick Members permission(s) to run this command.")


  #Ban
  @commands.command(name="ban")
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, member : discord.Member, * ,reason = None):
    try:
      await member.ban(reason=reason)
      await ctx.send(f"{member} has been banned by {ctx.author}.")
    except discord.ext.commands.errors.MissingPermissions:
      await ctx.send("You are missing Ban Members permission(s) to run this command.")



  # PING BOT
  @commands.command(name="ping")
  @commands.is_owner()
  async def ping(self,ctx):
    await ctx.send(f"[PING] {round(self.client.latency * 1000)}ms")


  @commands.command(name="setrole")
  @commands.has_permissions(manage_roles=True)
  async def setrole(self,ctx,member : discord.member, * ,role):
    await member.add_roles(role)
    await ctx.send(f'Role updated for {member}.')


  @commands.command(name="createrole")
  @commands.has_permissions(manage_roles=True)
  async def createrole(self,ctx, * , rolename):
    await ctx.guild.create_role(name=rolename)
    await ctx.send(f'{rolename} roeele created.')


def setup(client):
  client.add_cog(AdminCommands(client))