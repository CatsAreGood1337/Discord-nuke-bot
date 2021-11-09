import discord, os, asyncio, subprocess
from discord.ext import commands
from asyncio import sleep

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = "*", intents=intents)
client.remove_command("help")

@client.command()
async def load(ctx, extension):
		client.load_extension(f'cogs.{extension}')
		await ctx.send("cogs loaded...")

@client.command()
async def unload(ctx, extension):
		client.unload_extension(f'cogs.{extension}')
		await ctx.send("cogs loaded...")

@client.command()
async def reload(ctx, extension):
		client.unload_extension(f'cogs.{extension}')
		client.load_extension(f'cogs.{extension}')
		await ctx.send("cogs loaded...")

for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		client.load_extension(f'cogs.{filename[:-3]}')

client.run('token')