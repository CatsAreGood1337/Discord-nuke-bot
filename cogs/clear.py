import discord
from discord.ext import commands
from colorama import init, Fore, Back, Style

class User(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
    init()
	  pass

	@commands.command()
	async def clear(self, ctx, amount=1):
		await ctx.channel.purge(limit=amount)
		if amount == 1:
			print(Fore.GREEN + f"{amount} message cleared")
		else:
		  print(Fore.GREEN + f"{amount} messages cleared")
			
def setup(client):
	client.add_cog(User(client))