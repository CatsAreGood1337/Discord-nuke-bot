import discord, os
from discord.ext import commands
from last_fork.config import settings
from colorama import init, Fore

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = "*", intents=intents)
client.remove_command("help")

@client.command()
async def load(ctx, extension):
	client.load_extension(f'cogs.{extension}')
	await ctx.send(f"{extension} loaded...")
	print(Fore.GREEN + f'{ctx.message.author} loaded {extension}')

@client.command()
async def unload(ctx, extension):
	client.unload_extension(f'cogs.{extension}')
	await ctx.send(f"{extension} unloaded...")
	print(Fore.GREEN + f'{ctx.message.author} unloaded {extension}')

@client.command()
async def reload(ctx, extension):
	client.unload_extension(f'cogs.{extension}')
	client.load_extension(f'cogs.{extension}')
	await ctx.send(f"{extension} reloaded...")
	print(Fore.GREEN + f'{ctx.message.author} reloaded {extension}')

for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		client.load_extension(f'cogs.{filename[:-3]}')
		init()
		print(Fore.MAGENTA + f"{filename[:-3]} " + Fore.LIGHTBLACK_EX + "loaded")

print(Fore.BLUE + "ALL EXTENSIONS " + Fore.LIGHTBLACK_EX + "loaded")
  
client.run(settings['token'])