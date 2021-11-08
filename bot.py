import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = "*")
client.remove_command("help")

@client.command()
async def load(ctx, extension):
	if ctx.author.id == 410118481132912650:
		client.load_extension(f'cogs.{extension}')
		await ctx.send("cogs loaded...")
	else:
		await ctx.send("Вы не разработчик")

@client.command()
async def unload(ctx, extension):
	if ctx.author.id == 410118481132912650:
		client.unload_extension(f'cogs.{extension}')
		await ctx.send("cogs loaded...")
	else:
		await ctx.send("Вы не разработчик")

@client.command()
async def reload(ctx, extension):
	if ctx.author.id == 410118481132912650:
		client.unload_extension(f'cogs.{extension}')
		client.load_extension(f'cogs.{extension}')
		await ctx.send("cogs loaded...")
	else:
		await ctx.send("Вы не разработчик")

for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		client.load_extension(f'cogs.{filename[:-3]}')

client.run("token")