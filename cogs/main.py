import discord
from discord.ext import commands

class User(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print(1)

	@commands.command()
	async def info(self, ctx):
		await ctx.send("gay")

def setup(client):
	client.add_cog(User(client))