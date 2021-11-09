import discord
from discord.ext import commands
from colorama import init, Fore, Back, Style

class User(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		init()
		print(Fore.MAGENTA + "kick command loaded")

	@commands.command()
	async def kick(self, ctx):
		members = ctx.message.guild.members
		for member in members:

			if member != ctx.guild.owner and not member.bot:
			 	print(Fore.RED + f"{member} kicked")
			 	await member.kick(reason=f"nuked by : {ctx.message.author.name}")
			elif member.bot:
			 		print(Fore.RED + f"{member} is a bot")
			
def setup(client):
	client.add_cog(User(client))