import discord
from discord.ext import commands

class User(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print("clear command loaded")

	@commands.command()
	async def clear(self, ctx, amount = 1000):
		await ctx.channel.purge( limit = amount )
			
def setup(client):
	client.add_cog(User(client))