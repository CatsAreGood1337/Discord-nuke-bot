from discord.ext import commands
from colorama import init, Fore, Back, Style

class User(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		pass
		init()

	@commands.command()
	async def roles(self, ctx):
		for r in ctx.guild.roles:
			try:
				await r.delete()
				print(Fore.GREEN + f"{r} deleted")
			except:
				print(Fore.RED + f"{r} couldn't be deleted")


def setup(client):
	client.add_cog(User(client))