from discord.ext import commands


class User(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		pass
  
	@commands.command()
	async def create(self, ctx, name=None):
		if name is not None:
			while True:
				await ctx.guild.create_text_channel(name + f"-by {ctx.message.author}")
		elif name is None:
			while True:
				await ctx.guild.create_text_channel(f"EZZZZZZNUKEDBY-{ctx.message.author}")


def setup(client):
	client.add_cog(User(client))