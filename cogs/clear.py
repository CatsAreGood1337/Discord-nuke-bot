import discord
from discord.ext import commands
from colorama import init, Fore, Back, Style

class User(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		init()
		print(Fore.MAGENTA + "clear command loaded")

	@commands.command()
	async def clear(self, ctx, amount = 1000):
		await ctx.channel.purge( limit = amount )
		print(Fore.RED + "messages cleared")
			
def setup(client):
	client.add_cog(User(client))