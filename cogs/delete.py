from discord.ext import commands

class User(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		pass

	@commands.command()
	async def delete(self, ctx):
		for c in ctx.guild.channels:
			await c.delete()
		print("All channels deleted")
			
def setup(client):
	client.add_cog(User(client))