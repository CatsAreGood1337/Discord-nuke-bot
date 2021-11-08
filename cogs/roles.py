import discord
from discord.ext import commands


class User(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print("roles command loaded")

	@commands.command()
	async def roles(self, ctx):
		for r in ctx.guild.roles:
			try:
				r.delete()
			except:
				print("couldn't delete role")

def setup(client):
	client.add_cog(User(client))