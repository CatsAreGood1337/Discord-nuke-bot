import discord
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix="*", intents=intents)
client.remove_command("help")


@client.command()
async def load(ctx, extension):
	client.load_extension(f'cogs.{extension}')
	await ctx.send(f"{extension} loaded...")
	print(f'{ctx.message.author} loaded {extension}')

@client.command()
async def unload(ctx, extension):
	client.unload_extension(f'cogs.{extension}')
	await ctx.send(f"{extension} unloaded...")
	print(f'{ctx.message.author} unloaded {extension}')

@client.command()
async def reload(ctx, extension):
	client.unload_extension(f'cogs.{extension}')
	client.load_extension(f'cogs.{extension}')
	await ctx.send(f"{extension} reloaded...")
	print(f'{ctx.message.author} reloaded {extension}')

for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		client.load_extension(f'cogs.{filename[:-3]}')
		print(f"{filename[:-3]} loaded")

client.run('ur token here')
