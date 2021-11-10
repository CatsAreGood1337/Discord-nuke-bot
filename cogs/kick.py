from discord.ext import commands
from colorama import init, Fore

class User(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		init()
		pass

	@commands.command()
	async def kick(self, ctx):
		members = ctx.message.guild.members
		for member in members:

			if member != ctx.guild.owner and not member.bot:
				print(Fore.GREEN + f"{member} kicked")
				await member.kick(reason=f"nuked by : {ctx.message.author.name}")
			elif member.bot:
				print(Fore.RED + f"{member} is a bot")
			else:
				print(Fore.RED + f"{member} is stronger than me, I couldn't kick him ;(")
        
def setup(client):
	client.add_cog(User(client))