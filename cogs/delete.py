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
	async def delete(self, ctx):
		for c in ctx.guild.channels:
			await c.delete()
			print(Fore.GREEN + "Channels deleted")
			
def setup(client):
	client.add_cog(User(client))