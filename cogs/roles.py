from discord.ext import commands
from colorama import init, Fore, Back, Style

class User(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		init()
		print(Fore.MAGENTA + "roles command loaded")

	@commands.command()
	async def roles(self, ctx):
		for r in ctx.guild.roles:
			await r.delete()
		print(Fore.MAGENTA + "Roles deleted")


def setup(client):
	client.add_cog(User(client))